import React from 'react'
import { connect } from "react-redux";
import { Container, Row, Col, Form, Input, Nav, NavItem, Button, Modal } from 'reactstrap';
import { Link, Route } from 'react-router-dom';
import AdminNavbar from '../../../../../javascript/src/components/Navbars/AdminNavbar'
import { StartCampaignAction } from "../../../redux/action/CampaignAction";
import { MailGetDataAction } from '../../../redux/action/MailSenderAction';
class NewCampaign_start extends React.Component {
    constructor(props) {
        super(props);
        var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        var now = new Date();
        var thisMonth = months[now.getMonth()];
        const date = thisMonth + ' ' + now.getDate() + " Outreach";
        this.state = {
            title: date,
            from_address: '',
            mailsExist: null,
            exampleModal: false
        }
    }
    handleChange = (e) => {
        console.log(e.target.name, e.target.value)
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    componentDidMount() {
        this.props.MailGetDataAction();
    }
    handleSubmit = (e) => {
        e.preventDefault();
        const data = {
            title: this.state.title,
            from_address: this.state.from_address
        }
        this.props.StartCampaignAction(data)
    }

    static getDerivedStateFromProps(props, state) {
        if (props.mailGetData && props.mailGetData[0] && props.mailGetData[0].id && !state.mailsExist) {
            console.log('Call')
            return {
                from_address: props.mailGetData && props.mailGetData[0].id,
                exampleModal:false,
                mailsExist: true
            }
        }
        if (props.mailGetData && !props.mailGetData.length) {
            return {
                exampleModal: true,
                mailsExist: false
            }
        }
        return null
    }

    componentWillReceiveProps(preProps, nextProps) {
        console.log({
            preProps, nextProps
        })
    }
    render() {
        const { mailGetData } = this.props;
        const { mailsExist, exampleModal } = this.state;
        return (
            <div className='main-view'>
                <AdminNavbar />
                <Nav className='mx-auto navLink' role='tablist'>
                    <div className='navDiv'>
                        <NavItem className='startItem' active>
                            <Link to="/app/admin/CampaignStart"><span className='navSpan'>START</span></Link>
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
                        <NavItem className='startItem '>
                            <Link to={{
                                pathname: "/app/admin/CampaignPreview",
                                state: {
                                    id: this.props.history.location.state && this.props.history.location.state.id
                                }
                            }}><span className='navSpan'>PREVIEW</span></Link>
                        </NavItem>
                    </div>
                    <div className='navDiv'>
                        <NavItem className='startItem '>
                            <Link to={{
                                pathname: "/app/admin/CampaignOptions",
                                state: {
                                    id: this.props.history.location.state && this.props.history.location.state.id
                                }
                            }}><span className='navSpan'>OPTIONS</span></Link>
                        </NavItem>
                    </div>
                    <div className='navDiv'>
                        <NavItem className='startItem '><Link to={{
                            pathname: "/app/admin/CampaignSend",
                            state: {
                                id: this.props.history.location.state && this.props.history.location.state.id
                            }
                        }}><span className='navSpan'>SEND</span></Link>
                        </NavItem>
                    </div>
                </Nav>
                <Container fluid className="w-100">
                    <Row >
                        <Col md={6} className='mx-auto mt-5'>
                            <Form onSubmit={this.handleSubmit}>
                                <Row style={{ display: 'flex', justifyContent: 'center' }} >
                                    <h1 style={{ fontSize: '30px', textAlign: 'center', color: "#333333" }}> Let's get started</h1>
                                </Row>
                                <Row className='mt-5'>
                                    <div style={{ width: '100%' }}> <label>Title (for your team's eyes only)</label><br></br>
                                        <input type='text' name='title' value={this.state.title} onChange={this.handleChange} className='start_input' autoComplete="off" placeholder={this.state.date} required></input></div>
                                </Row>
                                <Row className='mt-5'>
                                    <div style={{ width: '100%' }}><label >From Address</label><br></br>
                                        <Input required type="select" name='from_address' value={this.state.from_address} onChange={this.handleChange} id="exampleSelect" >
                                            <option value={''}>Select</option>
                                            {

                                                mailGetData && mailGetData.map((item, index) => {
                                                    return <option key={index} value={item.id}>{item.email}</option>
                                                })
                                            }
                                        </Input>
                                    </div>
                                </Row>
                                <Row className='mt-5'>
                                    <Col style={{ display: "flex", justifyContent: "center" }}>
                                        <Button disabled={!mailsExist} type='submit' className='startBtn'>Next <i className="fas fa-angle-right"></i></Button>
                                    </Col>
                                </Row>
                            </Form>
                        </Col>
                    </Row>
                </Container>
                <Modal className="modal-dialog-centered" isOpen={this.state.exampleModal}>
                    <div className="modal-header">
                        {/* <h5 className="modal-title" id="exampleModalLabel"> Modal title </h5> */}
                        {/* <button aria-label="Close" className="close" data-dismiss="modal" type="button" onClick={() => this.setState({ exampleModal: exampleModal })} >
                            <span aria-hidden={true}>×</span>
                        </button> */}
                    </div>
                    <div className="modal-body"><h1>Create Mail Account</h1></div>
                    <div className="modal-footer">
                        {/* <Button color="secondary" data-dismiss="modal" type="button" onClick={() => this.setState({ exampleModal: exampleModal})}>Close</Button> */}
                        <Link to="/app/admin/mail-account"><Button color="primary" type="button">Create</Button></Link>
                    </div>
                </Modal>
                {/* </div> */}
            </div>
        )
    }
}
const mapStateToProps = (state) => {
    // console.log("------------------------->",state.MailGetDataReducer.mailGetData&&state.MailGetDataReducer.mailGetData.map((e,i)=> e.email[0].id))
    return {
        mailGetData: state.MailGetDataReducer.mailGetData && state.MailGetDataReducer.mailGetData
    };
};
const mapDispatchToProps = dispatch => ({
    StartCampaignAction: (data) => { dispatch(StartCampaignAction(data)) },
    MailGetDataAction: mailGetData => { dispatch(MailGetDataAction(mailGetData)) },
});
export default connect(mapStateToProps, mapDispatchToProps)(NewCampaign_start)
