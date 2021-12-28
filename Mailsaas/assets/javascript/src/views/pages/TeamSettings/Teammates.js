import React, { Component } from 'react'
// import Container from 'reactstrap/lib/Container'
import { Container, Row, Col, Table } from 'reactstrap'

export class Teammates extends Component {
    render() {
        return (
            <div>
                <div className='campaign_navbar' >
                        <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Your team</h1>
                        <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i class="fa fa-question-circle-o" aria-hidden="true"></i></p>
                    </div>
                <Container fluid>
                    <Row className="mt-5">
                        <Col md="8">
                            <Row className="ml-1 mb-3" style={{ color: "#333" }}>Administrators can update billing, connect new mail accounts, and invite people.</Row>
                            <Table responsive hover>
                                <thead>
                                    <tr>
                                        <th className="name">Name</th>
                                        <th className="Email">Email</th>
                                        <th className="IsAdmin">IS ADMIN</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr className='' >
                                        <td className="name-value">Omaid Faizyar</td>
                                        <td className="Email-value">omaid@faizyar.com</td>
                                        <td className="IsAdmin-value">Yes</td>
                                    </tr>
                                </tbody>
                            </Table>
                        </Col>
                        <Col md='4' style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>
                            <div style={{ margin: '17px 0px 24px 24px' }}>
                                <div className='dv1'>
                                    <Row>
                                        <h1>Team Information</h1>
                                    </Row>
                                    <Row style={{ fontSize: '16px', color: '#005aac' }} className='mt-3'>Add someone</Row>
                                    <Row ><input className='fullname-input' type='text' placeholder='Their full name'></input></Row>
                                    <Row className="mt-3"><input className='email-input' type='text' placeholder='Their email address'></input></Row>
                                    <Row className='mt-3'>
                                         <Col md='1'>  <input className='teamname-input' style={{width:"20px",height:"26px"}} type='checkbox'></input></Col> 
                                         <Col md='11'><p>Make administrator</p></Col> 
                                    </Row>
                                    <Row className='mt-3'>
                                        <button className='send-invite'>SEND INVITE</button>
                                    </Row>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Container>
            </div>
        )
    }
}

export default Teammates
