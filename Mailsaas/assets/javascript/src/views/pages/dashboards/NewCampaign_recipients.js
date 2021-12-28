import React, { Component } from 'react'
import { connect } from "react-redux";
import { Container, Row, Col, Button, Input, Nav, Form, NavItem } from 'reactstrap';
import { Link, Route } from 'react-router-dom';
import AdminNavbar from "../../../../../javascript/src/components/Navbars/AdminNavbar"
import { RecipientAction, StartCampaignAction } from "../../../redux/action/CampaignAction";
import Csvfile from './csvfile'

class NewCampaign_recipients extends Component {
    constructor(props) {
        super(props)
        this.state = {
            show: false,
            csvFile: '',
            email: [],
            options: [],
            campaign: this.props.history.location.state && this.props.history.location.state.id,
        }
    }
    handleChange = (e) => {
        this.setState({
            csvFile: e.target.files[0],
            show: true
        });
    }
    handleSubmit = (e) => {
        e.preventDefault();
        this.state.options.length = 0
        if (!this.state.email && !this.state.csvFile) {
            alert('Fill option 1 or 2')

            return false;
        }
        else if (this.state.csvFile && !this.state.email) {
            let temp = 1;
            this.state.options.push(temp)
        }
        else if (this.state.email && !this.state.csvFile) {
            let temp = 2;
            this.state.options.push(temp)
        }
        else if (this.state.csvFile && this.state.email) {
            let temp1 = 1;
            let temp2 = 2;
            this.state.options.push(temp1, temp2)
        }
        else { 
            this.setState({
               })
            return false 
        }
        const recipientData = {
            csvfile_op1: this.state.csvFile,
            option: `[${this.state.options}]`,
            email: `["${this.state.email}"]`,
            campaign: this.state.campaign
        }
        console.log(this.state.csvFile, 'file')

        this.props.RecipientAction(recipientData)
    }

    render() {
        const { show } = this.state;
        console.log(this.props.location, this.props.campaignDetails, "recipient")
        return (
            <>
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
                                <Link to="/app/admin/CampaignRecipient"><span className='navSpan'>RECIPICIENT</span></Link>
                            </NavItem>
                        </div>
                        <div className='navDiv'>
                            <NavItem className='startItem '><Link to={{
                                pathname:
                                    "/app/admin/CampaignCompose",
                                state: {
                                    id: this.props.history.location.state && this.props.history.location.state.id
                                }
                            }}><span className='navSpan'>COMPOSE</span></Link>
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
                    <Container fluid className="w-100">
                        <Row>
                            <Col md={12}>
                                <Form onSubmit={this.handleSubmit}>
                                    <Container fluid>
                                        <Row className='mt-5'>
                                            <Col><h1 style={{ fontSize: '30px', fontWeight: '200', textAlign: 'center', color: 'black' }}>Drop in your first list of recipients</h1></Col>
                                        </Row>
                                        <Row className='mt-5'>
                                            <Col md={6} className="receipentlist_box mx-auto">
                                                <div className="receipentlist_data_box" >
                                                    <div className="option1_container">
                                                        <Row className='mt-3'>
                                                            <Col md={3}><span className="option1">OPTION #1</span></Col>
                                                            <Col md={9}><Row>
                                                                <span className="csv_logo"><i className="fa fa-file" aria-hidden="true"></i></span>
                                                                <span className="csv_logo_text">Drop a CSV file here</span>
                                                                <span className="choose_option"><Input type='file' name='csvFile' value={this.state.value} onChange={this.handleChange}></Input></span></Row>
                                                                <Row><span>Campaigns are limited to 5k recipients; uploads to 1MB.</span></Row></Col>
                                                        </Row>
                                                        <Row className='mt-5'>
                                                            <Col md={3} className="option1"><span>OPTION #2</span></Col>
                                                            <Col md={9}><span><textarea type="email" style={{ background: 'transparent' }} name='email' value={this.state.email}
                                                                onChange={(e) => { this.setState({ show: true, email: e.target.value }) }} placeholder="type here"></textarea>
                                                                {show && <Button className='startBtn'>IMPORT</Button>}</span></Col>
                                                        </Row>
                                                    </div>
                                                </div>
                                            </Col>
                                        </Row>
                                    </Container>
                                </Form>
                            </Col>
                        </Row>
                    </Container>
                </div >
            </>
        )
    }
}
const mapStateToProps = (state) => {
    return {
        campaignDetails: state.StartCampaignReducer.startCampaignData.id,
        mailGetData: state.MailGetDataReducer.mailGetData
    };
};
const mapDispatchToProps = dispatch => ({
    RecipientAction: (recipientData) => { dispatch(RecipientAction(recipientData)) },
});

export default connect(mapStateToProps, mapDispatchToProps)(NewCampaign_recipients)
