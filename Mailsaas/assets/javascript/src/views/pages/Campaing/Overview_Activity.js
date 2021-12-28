import React from 'react'
import { Container, Row, Col, Table, Nav, NavItem, NavLink, TabContent, TabPane, } from 'reactstrap'

export default function Overview_Activity() {
    return (
        <div>
            <Container>
                <Row className='mt-5'>
                    <Col md={3}>
                        <select className='select_overview'>
                            <option>All recipient lists</option>
                            <option>Ignore sends</option>
                        </select>
                    </Col>
                </Row>
                <Row>
                    <div>

                    </div>
                </Row>
            </Container>
        </div>
    )
}
