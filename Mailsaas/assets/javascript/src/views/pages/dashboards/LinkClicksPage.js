import React from 'react';
import { Container, Row, Col, Input } from 'reactstrap';
import { Editor } from 'react-draft-wysiwyg';
import { EditorState, convertToRaw } from 'draft-js';
import draftToHtml from 'draftjs-to-html';
import htmlToDraft from 'html-to-draftjs';

export default class FollowUpPage extends React.Component {
    constructor() {
        super();
        this.state = {
            editorState: EditorState.createEmpty(),
            subject: '',
            waitDays: 0,
            body: '',
            url:''
        }
    }
    onEditorStateChange = (editorState) => {
        this.setState({ editorState })
    }
    handleChangeBody = (event) => {
        this.setState({
            body: event.blocks[0].text
        })
        console.log( event.blocks[0].text)
        Object.assign(this.props.onClickPageObject, { 'email_body': event.blocks[0].text })
    }
    handleSubject = (event) => {
        this.setState({
            subject: event.target.value
        })
        console.log(  event.target.value )

        Object.assign(this.props.onClickPageObject, { 'subject': event.target.value })
    }

    handleWaitDays = (event) => {
        this.setState({
            waitDays: event.target.value
        })
        console.log(  event.target.value )
        Object.assign(this.props.onClickPageObject, { 'waitDays': event.target.value })
    }
    onUrlChange=(event)=>{
        this.setState({
            url: event.target.value
        })
        console.log(  event.target.value )
        Object.assign(this.props.onClickPageObject, { 'url': event.target.value })
    }
    render() {
        const { editorState } = this.state;
        const { key } = this.props;
        return (
            <div>
                <Container fluid>
                    <Row>
                        <Col md={11} className='alignRight'>
                            <Row>
                                <h1 className='display-6'>On Link Clicks &nbsp;<a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                    <span><i className='QuestionCircle' class="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                </a></h1>
                            </Row>
                            <Row>
                                <p style={{ fontSize: '14px' }}>These emails are sent when a recipient clicks a link in one of your sent messages.</p>
                            </Row>
                            <Row>
                                <Col md={4}>
                                    <label className='filter_app_new'>Wait X days</label><br></br>
                                    <input value={this.state.waitDays} onChange={this.handleWaitDays} type='number'></input>
                                </Col>
                                <Col md={8}>
                                    <Input type='text' onChange={this.onUrlChange} value={this.state.url} className='in mt-3' style={{ borderBottom: '1px solid' }} placeholder='Clicked link url must exactly match:' required />
                                </Col>
                            </Row>
                            <Row></Row>
                            <Row className='mt-3'>
                                <div className='grand_parent'>
                                    <div className='input_field'>
                                        <Input type='text' onChange={this.handleSubject} value={this.state.subject} className='in' placeholder='Subject' required />
                                        <div className='mt-3'>
                                            <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                                <span><i className="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </Row>
                            <Row className='mt-3'>
                                <div className='Editor_div'>
                                <div style={{padding:0}} id={key-1} className="btn" onClick={this.onDeleteList}><i style={{padding:5}} className="fa">&#xf014;</i>DELETE</div>
                                    <Editor
                                        value={this.state.body}
                                        onChange={this.handleChangeBody}
                                        className='editorDiv'
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
