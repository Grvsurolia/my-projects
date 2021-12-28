import React from 'react'
import { Container, Row } from 'reactstrap'

function Domainpage() {
    return (
        <div>
            <Container fluid>
                <Row className="mt-3">
            <p style={{color:"black"}}>Search returned 0 unsubscribed domains.</p>
            </Row>
            </Container>
            
        </div>
    )
}

export default Domainpage
