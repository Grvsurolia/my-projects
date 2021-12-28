import React, { Component } from 'react'
import { Row, Col, Container, Button } from 'reactstrap'

export class Setting extends Component {
    render() {
        return (
            <div>
                <div className='campaign_navbar' >
                        <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Team settings</h1>
                        <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i class="fa fa-question-circle-o" aria-hidden="true"></i></p>
                    </div>
                <Container fluid >
                    <Row className='mt-3'>
                        <Col md={4} style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                            <div style={{ margin: '17px 0px 24px 24px' }}>
                                <div className='dv1'>
                                    <Row>
                                        <h1>Team Information</h1>
                                    </Row>
                                    <Row style={{ fontSize: '16px', color: '#005aac' }} className='mt-5'>Team Name</Row>
                                    <Row ><input className='teamname-input' type='text'></input></Row>
                                    <Row className='mt-3'>
                                        <button className='savebutton'>save</button>
                                        <button className='deleteteambutton mr-3'>delete team</button>
                                    </Row>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Container>
                <Container fluid >
                    <Row className='mt-5' style={{ color: '#777c', fontSize: '24px' }}>SENDING SETTINGS</Row>
                    <Row className='mt-5'>
                        <Col md={3} className='mr-3' style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                            <div style={{ margin: '17px 0px 24px 24px' }}>
                                <div className='dv1'>
                                    <Row>
                                        <h1>Custom tracking domains</h1>
                                    </Row>
                                    <Row>Use your own domain to track opens and clicks.</Row>
                                    <Row className='mt-5'><a href=''></a>Learn how his works</Row>
                                    <Row className='mt-3'>
                                        <Col>
                                            <ol>
                                                <li>Use your DNS provider to create a CNAME record that points to tracking.mailshake.com</li>
                                                <li>Enter your sub-domain below save these changes</li>
                                            </ol>
                                        </Col>
                                    </Row>
                                    <Row className='mt-3'>tracing.mailsaas.com</Row>
                                    <Row className='mt-3' style={{ border: '1px solid blue', width: "97%" }}>box</Row>

                                    <Row className='mt-5'><input className='teamname-input' type='text' placeholder='Your domain name'></input></Row>
                                    <Row className='mt-5'> <button className='savebutton'>save</button></Row>
                                </div>
                            </div>
                        </Col>
                        <Col md={3} style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                            <div style={{ margin: '17px 0px 24px 24px' }}>
                                <div className='dv1'>
                                    <Row>
                                        <h1>Campaign settings</h1>
                                    </Row>
                                    <Row ><input className='teamname-input' type='text' placeholder='Bcc every email'></input></Row>
                                    <Row className='mt-5' style={{ display: 'flex', flexDirection: 'column' }}>
                                        <label>show list-cleaning feature?</label>
                                        <select className='teamname-input'>
                                            <option>Yes</option>
                                            <option selected>No</option>
                                        </select>
                                    </Row>
                                    <Row className='mt-5' style={{ display: 'flex', flexDirection: 'column' }}>
                                        <Row>
                                            <Col style={{ display: "flex" }}>
                                                <label>How should unsubscribe link works</label>
                                                <label>?</label>
                                            </Col>
                                        </Row>
                                        <select className='teamname-input'>
                                            <option>Yes</option>
                                            <option selected>No</option>
                                        </select>
                                    </Row>
                                    <Row className='mt-5' style={{ display: 'flex', flexDirection: 'column' }}>
                                        <label>Enable mailassas dialer</label>
                                        <select className='dialer-input'>
                                            <option>Yes</option>
                                            <option selected>No</option>
                                        </select>
                                    </Row>
                                    <Row className='mt-5' style={{ display: 'flex', flexDirection: 'column' }}>
                                        <label>looking to hookup your CRM?</label>
                                    </Row>
                                    <Row className='mt-5'> <button className='savebutton'>save</button></Row>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Container>
                <Container fluid>
                    <Row className="mt-5">
                        <Col md={4}>
                            <ol className="links">
                                <li>  <Row className="mt-5 mb-5 ml-1" style={{ fontSize: "24px", color: "#777" }}>USEFUL LINKS</Row></li>
                                <li>CHANGE TEAMMATES</li>
                                <li>UPDATE BILLING</li>
                                <li>YOUR PERSONAL SETTINGS</li>
                            </ol>
                        </Col>
                    </Row>
                </Container>
            </div>
        )
    }
}

export default Setting
