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
        }
    }
    onEditorStateChange = (editorState) => {
        this.setState({ editorState })
    }
    handleChangeBody = (event) => {
        this.setState({
            body: event.blocks[0].text
        })
        Object.assign(this.props.dripPageObject, { 'email_body': event.blocks[0].text })
    }
    handleSubject = (event) => {
        this.setState({
            subject: event.target.value
        })
        Object.assign(this.props.dripPageObject, { 'subject': event.target.value })
    }

    handleWaitDays = (event) => {
        this.setState({
            waitDays: event.target.value
        })
        Object.assign(this.props.dripPageObject, { 'waitDays': event.target.value })
    }
    render() {
        const { editorState } = this.state;
        return (
            <div>
                <Container fluid>
                    <Row>
                        <Col md={11} className='alignRight'>
                            <Row>
                                <h1 className='display-6'>Drips &nbsp;<a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                    <span><i className='QuestionCircle' class="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                </a></h1>
                            </Row>
                            <Row>
                                <p style={{ fontSize: '14px' }}>Unlike follow-ups, drips keep sending even after a recipient becomes a lead.<a href=''>Learn how to customize Lead Catcher.</a></p>
                            </Row>
                            <Row>
                                <Col md={2} className='WaitDiv'>
                                    <label className='filter_app_new'>Wait X days</label><br></br>
                                    <input value={this.state.waitDays} onChange={this.handleWaitDays}  type='number' className='WaitInput'></input>
                                </Col>
                            </Row>
                            <Row> <p style={{ fontSize: '14px' }}> Drips don't wait on follow-ups. This counts days from your initial message.</p></Row>
                            <Row>
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
                                <div style={{padding:0}} className="btn" onClick={this.onDeleteList}><i style={{padding:5}} className="fa">&#xf014;</i>DELETE</div>
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
