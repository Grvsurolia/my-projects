import React from 'react';
import { Container, Row, Col, Input} from 'reactstrap';
import { Editor } from 'react-draft-wysiwyg';
import { EditorState } from 'draft-js';


export default class FollowUpPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            editorState: EditorState.createEmpty(),
            waitDays: 0,
            replyChain:this.props.normalSubject,
            body:'',
            subjectOfFollowUp:'',
            newSubject:''
        }
    }
   componentDidMount(){
    Object.assign(this.props.followUpPageObject,{'subject':this.state.replyChain})
    Object.assign(this.props.followUpPageObject,{'waitDays':this.state.waitDays})
    Object.assign(this.props.followUpPageObject,{'email_body':this.state.body})

   }
    handleChangewaitDays = (event) =>{
        this.setState({
            waitDays: event.target.value
        })
        Object.assign(this.props.followUpPageObject,{"waitDays": event.target.value});
    }

    handleChangeReplyChain = (event) => {
        if (this.props.normalSubject===event.target.value) {
            this.setState({
                subjectOfFollowUp:'',
                replyChain: event.target.value
            })
        Object.assign(this.props.followUpPageObject,{'subject':event.target.value})
        } else {
            this.setState({
                replyChain: event.target.value
            })  
        }
        
    }
    
    handleFollowSubject =(event) =>{
        this.setState({
            subjectOfFollowUp: event.target.value
        })
        Object.assign(this.props.followUpPageObject,{'subject':event.target.value})
    }

    handleChangeBody = (event) => {
        this.setState({
            body: event.blocks[0].text
        })
        Object.assign(this.props.followUpPageObject,{'email_body':this.state.body})
    }

    onEditorStateChange = (editorState) => {
        this.setState({ editorState })
    }

    render() {
        const { editorState } = this.state;
        const { id } = this.props;

        return (
            <div key={id}>
                <Container fluid>
                    <Row>
                        <Col md={11} className='alignRight'>
                            <Row>
                                <h1 className='display-6'>Follow-ups &nbsp;<a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                    <span><i className='QuestionCircle' className="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                </a></h1>
                            </Row>
                            <Row>
                                <p style={{ fontSize: '14px' }}>Follow-ups are stopped when a recipient becomes a lead. <a href=''>Learn how to customize Lead Catcher.</a></p>
                            </Row>
                            <Row>
                                <Col md={2} className='WaitDiv'>
                                    <label className='filter_app_new'>Wait X days</label><br></br>
                                    <input value={this.state.waitDays} onChange={this.handleChangewaitDays} type='number' className='WaitInput'></input>
                                </Col>
                            </Row>
                            <Row className='mt-3'>
                                <label className='filter_app_new'>Reply Chain</label><br></br>
                                <div className='select_div'>
                                    <select  name="subject"  value={this.state.replyChain} onChange={this.handleChangeReplyChain} className='filter_select_prospect'>
                                        <option value={this.props.normalSubject}>{this.props.normalSubject}</option>
                                        <option placeholder="---New Email---" value="new-email">---New Email---</option>
                                    </select>
                                    {
                                        this.state.replyChain==='new-email' &&
                                        <Input onChange={this.handleFollowSubject} type='text' className='in' name='subject' value={this.state.SubjectOfFollowUp} placeholder='Subject' />
                                    }
                                </div>
                            </Row>
                            <Row className='mt-3'>
                                <div className='Editor_div'>
                                    <div style={{padding:0}} className="btn" onClick={()=>this.props.onDeleteList(id)}><i style={{padding:5}} className="fa">&#xf014;</i>DELETE {id}</div>
                                    <Editor
                                        className='editorDiv'
                                        onChange={this.handleChangeBody}
                                        value={this.state.body}
                                        editorState={editorState}
                                        toolbarClassName="rdw-storybook-toolbar"
                                        wrapperClassName="rdw-storybook-wrapper"
                                        editorClassName="rdw-storybook-editor"
                                        onEditorStateChange={this.onEditorStateChange}
                                        toolbar={{
                                            link: {
                                                defaultTargetOption: '_blank',
                                            },
                                        }}
                                    />
                                </div>
                            </Row>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}
