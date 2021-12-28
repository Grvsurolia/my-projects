import React, { Component } from 'react'
import { Container, Row, Col } from 'reactstrap'
import Teammates from './Teammates'
export class Redeem extends Component {
    render() {
        return (
            <div>
                <div className='campaign_navbar' >
                    <h1 style={{ color: 'white', fontSize: '20px', marginLeft: '20px', marginTop: "20px" }}>Redeem a promotion</h1>
                    <p style={{ color: "white", fontSize: "20px", marginTop: "20px", marginRight: "20px" }}><i class="fa fa-question-circle-o" aria-hidden="true"></i></p>
                </div>
                <Container fluid>
                    <Row>
                        <Col md="4">
                            <Row className=" mt-3 " style={{ color: "#333" }}>Do you have a promo code? Apply it to your team:{ }</Row>
                        </Col>
                    </Row>
                </Container>
                <Container fluid >
                    <Row className='mt-3'>
                        <Col md='4' style={{ border: '1px solid #ccc', background: 'white', boxShadow: '0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.12)' }}>

                            <div className='dv1'>
                                <Row className='ml-2 mt-4' ><input className='teamname-input' type='text' placeholder="Promo code"></input></Row>
                                <div>
                                    <Row className='mt-3 ml-2 mb-3'>
                                        <button className='savebutton' style={{ width: "8em" }}>APPLYPROMO</button>
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

export default Redeem
