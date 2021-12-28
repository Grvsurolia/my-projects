import React, { Component } from 'react'
import { Container, Row, Button, Input, Col, Form, Nav, NavItem, NavLink } from 'reactstrap';
import { Editor } from 'react-draft-wysiwyg';
import { Link } from 'react-router-dom';
import { EditorState } from 'draft-js';
import FollowUpPage from './FollowUpPage';
import Drips from './Drips'
import LinkClicksPage from './LinkClicksPage'
import { connect } from 'react-redux';
import { CampaignComposeAction } from '../../../redux/action/CampaignAction';
import { Alert } from 'reactstrap';
import AdminNavbar from "../../../../../javascript/src/components/Navbars/AdminNavbar"
class CampaignCompose extends Component {
    constructor() {
        super();
        this.state = {
            subject: '',
            email_body: '',
            editorState: EditorState.createEmpty(),
            inputListFollow: [],
            inputListDrips: [],
            inputListLinkClick: [],
            dataObj: {},
            arra: [],
            followUpData: [],
            dripData: [],
            onClickData: [],
            dripPageObject: {},
            normalData: {},
            isOpen: false
        }
        this.counter = 0
    }

    handleSubject = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
        Object.assign(this.state.normalData, { 'subject': e.target.value })
    }
    onAddBtnClickFollow = () => {
        const inputListFollow = this.state.inputListFollow;
        this.counter = this.counter + 1
        this.state.counter === 0 ? null : this.state.followUpData.push(this.state.dataObj)
        this.setState({
            dataObj: {},
            inputListFollow: inputListFollow.concat(<FollowUpPage onDeleteList={this.onDeleteList} msgBody={this.state.msgBody} followUpPageObject={this.state.dataObj} normalSubject={this.state.subject} id={this.counter} />),
        });
    }
    onAddBtnClickDrips = () => {
        const inputListDrips = this.state.inputListDrips;
        this.counter = this.counter + 1
        this.state.counter === 0 ? null : this.state.dripData.push(this.state.dataObj)
        this.setState({
            dataObj: {},
            inputListDrips: inputListDrips.concat(<Drips dripPageObject={this.state.dataObj} key={this.counter} onDeleteList={this.onDeleteList} />)
        });
    }
    onAddBtnClickLinkClick = () => {
        const inputListLinkClick = this.state.inputListLinkClick;
        const inputListDrips = this.state.inputListDrips;
        this.counter = this.counter + 1
        this.state.counter === 0 ? null : this.state.onClickData.push(this.state.dataObj)
        this.setState({
            dataObj: {},
            inputListLinkClick: inputListLinkClick.concat(<LinkClicksPage onClickPageObject={this.state.dataObj} onDeleteList={this.onDeleteList} key={this.counter} />)
        });
    }
    onEditorStateChange = (editorState) => {
        this.setState({ editorState })
    }
    handleSubmit = (e) => {
        e.preventDefault()
        if (this.state.email_body === '') {
            this.setState({
                isOpen: true
            })
        }
        else {
            Object.assign(this.state.normalData, { 'campaign': this.props.history.location.state && this.props.history.location.state.id })
            let data = {
                normal: this.state.normalData,
                follow_up: this.state.followUpData,
                drips: this.state.dripData,
                onLinkClick: this.state.onClickData
            }
            this.props.CampaignComposeAction(data)
        }

    }
    onChange = (e) => {
        this.setState({ msgBody: e.blocks[0].text })
    }
    handleMsgBody = (e) => {
        this.setState({
            email_body: e.blocks[0].text,
            isOpen: false
        })
        Object.assign(this.state.normalData, { 'email_body': e.blocks[0].text })
    }

    onDeleteList = (e) => {
        var array = [...this.state.inputListFollow];
        let index = e - 1;
        let a = this.state.inputListFollow.keys()
        console.log(e, "sgsd")
        //     const newList = array.filter((item,i) => i !== index);
        //     this.setState({
        //         inputListFollow:newList
        //     })
        //    this.counter=0
    }
    render() {
        const { editorState, inputListFollow } = this.state;

        console.log(inputListFollow, "compose")
        return (
            <div>

                <div className='main-view'>
                    <AdminNavbar />
                    <Nav className='mx-auto navLink' role='tablist'>
                        <div className='navDiv'>
                            <NavItem className='startItem' active>
                                <Link to={{
                                    pathname: "/app/admin/CampaignStart",
                                    state: {
                                        id: this.props.history.location.state && this.props.history.location.state.id
                                    }
                                }}><span className='navSpan'>START</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '>
                                <Link to={{
                                    pathname: "/app/admin/CampaignRecipient",
                                    state: {
                                        id: this.props.history.location.state && this.props.history.location.state.id
                                    }
                                }}><span className='navSpan'>RECIPICIENT</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '>
                                <Link to="/app/admin/CampaignCompose"><span className='navSpan'>COMPOSE</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '><Link to={{
                                pathname: "/app/admin/CampaignPreview",
                                state: {
                                    id: this.props.history.location.state && this.props.history.location.state.id
                                }
                            }}><span className='navSpan'>PREVIEW</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '><Link to={{
                                pathname: "/app/admin/CampaignOptions",
                                state: {
                                    id: this.props.history.location.state && this.props.history.location.state.id
                                }
                            }}><span className='navSpan'>OPTIONS</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '>
                                <Link to={{
                                    pathname: "/app/admin/CampaignSend",
                                    state: {
                                        id: this.props.history.location.state && this.props.history.location.state.id
                                    }
                                }}><span className='navSpan'>SEND</span></Link>
                            </NavItem>
                        </div>
                    </Nav>
                    <Form onSubmit={this.handleSubmit} >
                        <Container fluid>
                            <Row>
                                <Col md={10} className='mx-auto'>
                                    <Row className="composeemail_heading">
                                        Compose the emails in this campaign
                                </Row>
                                    <Row className="mt-5">
                                        <div><button className='EditTest'><i className="fa fa-plus-circle" aria-hidden="true"></i> A/B TEST</button>
                                        </div>
                                    </Row>
                                    <Row>
                                        <div className='grand_parent'>
                                            <div className='input_field'>
                                                <Input type='text' className='in' name='subject' value={this.state.subject} onChange={this.handleSubject} placeholder='Subject' required />
                                                <div className='mt-3'>
                                                    <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                                        <span><i className="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </Row>
                                    <Row>
                                        <div className='Editor_div'>
                                            <Editor
                                                className='editorDiv'
                                                style={{height:'210px'}}
                                                editorState={editorState}
                                                toolbarClassName="rdw-storybook-toolbar"
                                                wrapperClassName="rdw-storybook-wrapper"
                                                editorClassName="rdw-storybook-editor"
                                                name='email_body'
                                                value={this.state.email_body}
                                                onChange={this.handleMsgBody}
                                                onEditorStateChange={this.onEditorStateChange}
                                                required
                                            />
                                        </div>
                                    </Row>
                                    <Row className='mt-5'>
                                        {this.state.inputListFollow}
                                    </Row>

                                    <Row>
                                        <Col className='mt-3'>
                                            <div className='Add_follow_up' onClick={this.onAddBtnClickFollow}>
                                                <i className='fa fa-plus'></i> &nbsp;ADD FOLLOW-UP<br />
                                            </div>
                                        </Col>
                                    </Row>
                                    <Row>
                                        {this.state.inputListDrips}
                                    </Row>
                                    <Row>
                                        <Col className='mt-3'>
                                            <div className='Add_follow_up' onClick={this.onAddBtnClickDrips}>
                                                <i className='fa fa-plus'></i> &nbsp;ADD DRIP<br />
                                            </div>
                                        </Col>
                                    </Row>
                                    <Row>
                                        {this.state.inputListLinkClick}
                                    </Row>
                                    <Row>
                                        <Col className='mt-3 mb-5'>
                                            <div className='Add_follow_up' onClick={this.onAddBtnClickLinkClick}>
                                                <i className='fa fa-plus'></i> &nbsp;ADD ON CLICK<br />
                                            </div>
                                        </Col>
                                    </Row>
                                    <Row className='mx-auto'>
                                        <Button className='startBtn'>CANCEL</Button>
                                        <Button className="startBtn" type='submit' >NEXT<i className="fa fa-arrow-right" aria-hidden="true"></i></Button>
                                    </Row>
                                </Col>
                            </Row>
                        </Container>
                    </Form>
                    <div style={{ display: 'flex', justifyContent: 'center', position: 'absolute', bottom: 0, right: 10 }}>
                        <Alert className="alert_" toggle={() => { this.setState({ isOpen: false }) }} isOpen={this.state.isOpen} color="warning">Initial message must have a body</Alert>
                    </div>
                </div>
            </div>
        )
    }
}
const mapStateToProps = (state) => {
    return {
        // campaign: state.StartCampaignReducer.startCampaignData && state.StartCampaignReducer.startCampaignData.id,
        // mailGetData: state.MailGetDataReducer.mailGetData
    }
}
const mapDispatchToProps = (dispatch) => ({
    CampaignComposeAction: (data) => dispatch(CampaignComposeAction(data))
})
export default connect(mapStateToProps, mapDispatchToProps)(CampaignCompose);