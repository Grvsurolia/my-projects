import React, { Component } from 'react'
import { Container, Row, Col } from 'reactstrap'
class Billing extends Component {
    render() {
        return (
            <div>
                <div className='campaign_navbar' >
                    <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Billing</h1>
                    <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i class="fa fa-question-circle-o" aria-hidden="true"></i></p>
                </div>
                <Container fluid >
                    <Row className='mt-3'>
                        <Col md='4' style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                            <div className='dv1'>
                                <Row>
                                    <h1 style={{ color: "green" }} className='ml-4'>ACTIVE PLAN</h1>
                                </Row>
                                <Row style={{ fontSize: '12px', color: '#005aac' }} className='mt-3 ml-2'>Renews On</Row>
                                <Row style={{ fontSize: '16px', color: 'rgba(0,0,0, 0.54)', fontWaight: "700" }} className='mt-0 ml-2'>Feb 11, 2021</Row>
                                <Row style={{ fontSize: '12px', color: '#005aac' }} className='mt-3 ml-2'>Plan type</Row>
                                <Row style={{ fontSize: '16px', color: 'rgba(0,0,0, 0.54)', fontWaight: "700" }} className='mt-0 ml-2'>Monthly Email Outreach</Row>
                                <Row style={{ fontSize: '12px', color: '#005aac' }} className='mt-3 ml-2'>Number of users</Row>
                                <Row style={{ fontSize: '16px', color: 'rgba(0,0,0, 0.54)', fontWaight: "700" }} className='mt-0 ml-2'>1</Row>
                                <Row className="mt-2" style={{ backgroundColor: "#ccc", borderTop: "1px solid #ccc", borderBottom: "1px solid #ccc" }}>
                                    <div style={{ width: "100%", display: "flex", padding: "10px 0px" }}>
                                        <div style={{ width: "50%", display: "flex", justifyContent: "flex-start", paddingLeft: "10px" }}>CHNGE</div>
                                        <div style={{ width: "45%", display: "flex", justifyContent: "flex-end" }}>
                                            <div><i class="fa fa-dollar-sign"></i></div>
                                            <div>59</div>
                                        </div>
                                    </div>
                                </Row>
                                <Row className='mt-3 ml-1 mb-3'>
                                    <button className='savebutton' style={{ width: "7em" }}>UPGRADE</button>
                                    <button className='deleteteambutton mr-3'>CHANGE</button>
                                </Row>
                            </div>
                        </Col>
                    </Row>
                </Container>
            </div>
        )
    }
}

export default Billing
