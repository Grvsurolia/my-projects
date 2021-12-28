import React, { Component } from 'react'
import { Container, Row, Nav, Input, Col,NavItem } from 'reactstrap';
import { Editor } from 'react-draft-wysiwyg';
import { Link, Route } from 'react-router-dom';
import { EditorState, convertToRaw, ContentState } from 'draft-js';
import { PreviewCampaignAction, PreviewUpdateCampaignAction } from "../../../redux/action/CampaignAction"
import { connect } from 'react-redux'
import AdminNavbar from "../../../../../javascript/src/components/Navbars/AdminNavbar"

class CampaignPreview extends Component {
    constructor() {
        super();
        this.state = {
            editorState: EditorState.createEmpty()
        }
    }
    onEditorStateChange = (editorState) => {
        this.setState({ editorState })
    }
    componentDidMount() {
        console.log(this.props.history.location.state && this.props.history.location.state.id, "preview")
        let id = this.props.history.location.state && this.props.history.location.state.id
        this.props.PreviewCampaignAction(id);
        this.props.PreviewUpdateCampaignAction(id)
    }
    render() {
        const { editorState } = this.state;
        const { CampaignEmail, CampaignFollowUp } = this.props;
        console.log(editorState, "preview")
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
                                <Link to={{
                                    pathname: "/app/admin/CampaignCompose",
                                    state: {
                                        mailGetData: this.props.mailGetData
                                    }
                                }}><span className='navSpan'>COMPOSE</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '><Link to="/app/admin/CampaignPreview"><span className='navSpan'>PREVIEW</span></Link>
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
                    <Container fluid>
                        <Row className='mt-3'>
                            <Col md={6} className="mx-auto">
                                <Row className="preview_email">Preview and personalize each email</Row>
                                <Row className="beforehitting_next">Before hitting next, make sure:</Row>
                                <Row style={{ display: "flex", justifyContent: "center" }}>
                                    <Row className="condition_container">
                                        <Row >
                                            <div style={{ display: "flex", flexDirection: "row" }} >
                                                <div className="rightcheck_icon"><i className="fa fa-check-circle" aria-hidden="true"></i></div>
                                                <div className="condition">You sound like a human</div>
                                            </div>
                                        </Row>
                                        <Row>
                                            <div style={{ display: "flex", flexDirection: "row" }} >
                                                <div className="rightcheck_icon"><i className="fa fa-check-circle" aria-hidden="true"></i></div>
                                                <div className="condition">Your signature looks good</div>
                                            </div>
                                        </Row>
                                        <Row>
                                            <div style={{ display: "flex", flexDirection: "row" }} >
                                                <div className="rightcheck_icon"><i className="fa fa-check-circle" aria-hidden="true"></i></div>
                                                <div className="condition">Your signature looks good</div>
                                            </div>
                                        </Row>
                                        <Row>
                                            <div style={{ display: "flex", flexDirection: "row" }} >
                                                <div className="rightcheck_icon"><i className="fa fa-check-circle" aria-hidden="true"></i></div>
                                                <div className="condition">Your call-to-action is clear</div>
                                            </div>
                                        </Row>
                                        <Row>
                                            <div style={{ display: "flex", flexDirection: "row" }} >
                                                <div className="rightcheck_icon"><i className="fa fa-check-circle" aria-hidden="true"></i></div>
                                                <div className="condition">You‘ve sent a test email and checked it on your phone</div>
                                            </div>
                                        </Row>
                                    </Row><Col>
                                    </Col>
                                    {/* </Col> */}
                                </Row>
                                <Row className='mt-5'>
                                    <Col style={{ display: "flex", justifyContent: "center" }}><Link to={{
                                        pathname: '/app/admin/CampaignOptions',
                                        state: {
                                            id: this.props.history.location.state && this.props.history.location.state.id
                                        }
                                    }} className='btn startBtn'>Next <i className="fa fa-arrow-right" aria-hidden="true"></i></Link></Col>
                                </Row>
                            </Col>
                        </Row>
                    </Container>
                    <Container>
                        <Row className="mt-3">
                            <Col md={12} className='mx-auto'>
                                <div style={{ backgroundColor: "#005aac", color: "white" }}>
                                    {
                                        <ul >
                                            {this.props.CampaignPreviewEmails && this.props.CampaignPreviewEmails.map((e, i) => <li style={{ color: 'white' }}>{e.email}</li>)}
                                        </ul>
                                    }
                                </div>
                            </Col>
                        </Row>
                    </Container>
                    <Container>
                        <Row>
                            {
                                this.props.CampaignPreviewEmails && this.props.CampaignPreviewEmails.map((item, index) => {
                                    return <div>
                                        <Col md={11} className='mx-auto'>
                                            <Row className='mt-3'>
                                                <div><i className="fa fa-envelope-o" aria-hidden="true"></i><label style={{ marginLeft: "5px" }}>Initial campaign email</label></div>
                                                <div className='grand_parent'>
                                                    <div className='input_field'>
                                                        <Input type='email' className='in' placeholder='Subject' key={index} value={item.subject} onChange={() => {

                                                        }} />
                                                        <div className='mt-3'>
                                                            <a href='' onClick={(e) => { e.preventDefault(); alert('msg') }}>
                                                                <span><i className="fa fa-question-circle-o" aria-hidden="true"></i></span>
                                                            </a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </Row>
                                            <Row className="mt-5 mb-5">
                                                <div className='Editor_div'>
                                                    <Editor
                                                        className='editorDiv'
                                                        readOnly
                                                        // mention={{
                                                        //     separator: ' ',
                                                        //     trigger: '@',
                                                        //     suggestions: [
                                                        //         { text: 'APPLE', value: 'apple', url: 'apple' },
                                                        //         { text: 'BANANA', value: 'banana', url: 'banana' },
                                                        //         { text: 'CHERRY', value: 'cherry', url: 'cherry' },
                                                        //         { text: 'DURIAN', value: 'durian', url: 'durian' },
                                                        //         { text: 'EGGFRUIT', value: 'eggfruit', url: 'eggfruit' },
                                                        //         { text: 'FIG', value: 'fig', url: 'fig' },
                                                        //         { text: 'GRAPEFRUIT', value: 'grapefruit', url: 'grapefruit' },
                                                        //         { text: 'HONEYDEW', value: 'honeydew', url: 'honeydew' },
                                                        //     ],                                                           
                                                        // }}
                                                        placeholder={item.email_body}
                                                        editorState={editorState}
                                                        value={item.email_body}
                                                        defaultContentState={"etertretertert"}
                                                        currentState={item.email_body}
                                                        toolbarClassName="rdw-storybook-toolbar"
                                                        wrapperClassName="rdw-storybook-wrapper"
                                                        editorClassName="rdw-storybook-editor"
                                                        initialEditorState={editorState}
                                                        onEditorStateChange={this.onEditorStateChange}
                                                        toolbar={{
                                                            link: {
                                                                defaultTargetOption: '_blank',
                                                            },
                                                        }}
                                                    />
                                                </div>
                                            </Row>
                                            <Row className='mb-3 '>
                                                {
                                                    this.props.CampaignFollowUp && this.props.CampaignFollowUp.map((item, index) => {
                                                        return <div>
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
                                                                        <input value={item.waitDays} type='number' className='WaitInput'></input>
                                                                    </Col>
                                                                </Row>
                                                                <Row className='mt-3 '>
                                                                    <label className='filter_app_new'>Reply Chain</label><br></br>
                                                                    <div className='select_div'>
                                                                        <Input value={item.subject} type='text' className='in' name='subject' placeholder='Subject' />
                                                                    </div>
                                                                </Row>
                                                                <Row className='mt-3'>
                                                                    <div className='Editor_div'>
                                                                        <div style={{ padding: 0 }} className="btn"><i style={{ padding: 5 }} className="fa">&#xf014;</i>DELETE</div>
                                                                        <Editor
                                                                            placeholder={item.email_body}
                                                                            className='editorDiv'
                                                                            onChange={this.handleChangeBody}
                                                                            editorState={editorState}
                                                                            toolbarClassName="rdw-storybook-toolbar"
                                                                            wrapperClassName="rdw-storybook-wrapper"
                                                                            editorClassName="rdw-storybook-editor"
                                                                            value={item.email_body}
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
                                                        </div>

                                                    })
                                                }

                                            </Row>
                                            <Row>
                                                {
                                                    this.props.CampaignDrip && this.props.CampaignDrip.map((item, index) => {
                                                        return <div>
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
                                                                        <input key={index} value={item.waitDays} type='number' className='WaitInput'></input>
                                                                    </Col>
                                                                </Row>
                                                                <Row> <p style={{ fontSize: '14px' }}> Drips don't wait on follow-ups. This counts days from your initial message.</p></Row>
                                                                <Row>
                                                                    <div className='grand_parent'>
                                                                        <div className='input_field'>
                                                                            <Input type='text' key={index} value={item.subject} className='in' placeholder='Subject' required />
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
                                                                        <div style={{ padding: 0 }} className="btn" onClick={this.onDeleteList}><i style={{ padding: 5 }} className="fa">&#xf014;</i>DELETE</div>
                                                                        <Editor
                                                                            onChange={this.handleChangeBody}
                                                                            className='editorDiv'
                                                                            editorState={editorState}
                                                                            toolbarClassName="rdw-storybook-toolbar"
                                                                            wrapperClassName="rdw-storybook-wrapper"
                                                                            editorClassName="rdw-storybook-editor"
                                                                            value={item.email_body}
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
                                                        </div>
                                                    })
                                                }
                                            </Row>
                                            <Row className='mb-3'>
                                                {
                                                    this.props.CampaignOnClick && this.props.CampaignOnClick.map((item, index) => {
                                                        return <div>

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
                                                                        <input value={item.waitDays} type='number'></input>
                                                                    </Col>
                                                                    <Col md={8}>
                                                                        <Input type='text' value={item.url} className='in mt-3' style={{ borderBottom: '1px solid' }} placeholder='Clicked link url must exactly match:' required />
                                                                    </Col>
                                                                </Row>
                                                                <Row></Row>
                                                                <Row className='mt-3'>
                                                                    <div className='grand_parent'>
                                                                        <div className='input_field'>
                                                                            <Input type='text' onChange={this.handleSubject} value={item.subject} className='in' placeholder='Subject' required />
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
                                                                        <div style={{ padding: 0 }} className="btn" onClick={this.onDeleteList}><i style={{ padding: 5 }} className="fa">&#xf014;</i>DELETE</div>
                                                                        <Editor
                                                                            value={this.state.body}
                                                                            onChange={this.handleChangeBody}
                                                                            className='editorDiv'
                                                                            editorState={editorState}
                                                                            toolbarClassName="rdw-storybook-toolbar"
                                                                            wrapperClassName="rdw-storybook-wrapper"
                                                                            editorClassName="rdw-storybook-editor"
                                                                            toolbar={item.email_body}
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

                                                        </div>

                                                    })
                                                }

                                            </Row>
                                        </Col>
                                    </div>
                                })}
                        </Row>
                    </Container>
                </div>
            </div>
        )
    }
}
const mapStateToProps = (state) => {
    console.log("-----------------------------------))))))", state.CampaignPreviewGetReducer.CampaignPreviewData)
    return {
        campaignId: state.StartCampaignReducer.startCampaignData.id,
        CampaignPreviewData: state.CampaignPreviewGetReducer.CampaignPreviewData,
        CampaignPreviewEmails: state.CampaignPreviewGetReducer.CampaignPreviewData && state.CampaignPreviewGetReducer.CampaignPreviewData.campEmail,
        CampaignFollowUp: state.CampaignPreviewGetReducer.CampaignPreviewData && state.CampaignPreviewGetReducer.CampaignPreviewData.follow_up,
        CampaignDrip: state.CampaignPreviewGetReducer.CampaignPreviewData && state.CampaignPreviewGetReducer.CampaignPreviewData.drip,
        CampaignOnClick: state.CampaignPreviewGetReducer.CampaignPreviewData && state.CampaignPreviewGetReducer.CampaignPreviewData.onLinkClick,
    }
}
const mapDispatchToProps = dispatch => ({
    PreviewCampaignAction: (recipientId) => { dispatch(PreviewCampaignAction(recipientId)) },
    PreviewUpdateCampaignAction: campaignPreviewUpdateData => { dispatch(PreviewUpdateCampaignAction(campaignPreviewUpdateData)) },
})
export default connect(mapStateToProps, mapDispatchToProps)(CampaignPreview)
