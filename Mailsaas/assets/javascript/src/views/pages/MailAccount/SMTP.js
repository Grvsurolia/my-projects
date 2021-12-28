import React, { Component } from 'react'
import { Button, Container, Modal, ModalHeader, ModalBody, ModalFooter, Row, Col, Input ,Form} from 'reactstrap';

export class SmtpModal extends Component {
    constructor(props) {
        super(props)
    }
componentWillUnmount(){
    console.group('unmount in model')
}
    render() {
        console.log(this.props.imapPassword,"props")
        return (
            <div>
                <Modal isOpen={this.props.isOpen} toggle={this.props.toggle} >
                    <Form onSubmit={this.props.handleSubmit}>
                        <ModalHeader toggle={this.props.toggle}><h1>Connect a mail account</h1><p>How will you be sending emails?</p></ModalHeader>
                        <ModalBody >
                            <Container>
                                <Row>
                                    <Col md={2}><i className="far fa-user s-4"  ></i></Col>
                                    <Col md={10}>
                                        <Row>Sending address</Row>
                                        <Row><p style={{ fontSize: '0.7em' }}>This will be the “from” name and address on your emails and must be an address allowed by your email provider.</p></Row>
                                        <Row><Input type='email' name='emailAddress' value={this.props.emailAddress} autoComplete='off' onChange={this.props.handleChange} placeholder='Email Address'></Input></Row><br></br>
                                        <Row><Input type='text' name='FullName' value={this.props.FullName} onChange={this.props.handleChange} placeholder='Full Name'></Input></Row>
                                    </Col>
                                </Row><br></br>
                                <Row>
                                    <Col md={2}><i className="far fa-paper-plane s-4"></i></Col>
                                    <Col md={10}>
                                        <Row>SMTP connection</Row>
                                        <Row><p style={{ fontSize: '0.7em' }}>This information comes from your email provider and is how we‘ll send your emails.</p></Row>
                                        <Row>
                                            <Col md={8}><Input name='smtpHost' value={this.props.smtpHost} onChange={this.props.handleChange} className='mt-4' type='text' placeholder='Host(e.g.mail.server.com)'></Input></Col>
                                            <Col md={4}><label className='selectbox_label' >Port Number</label>
                                                <Input name='smtpPort' type='select' onChange={this.props.handleChange} defaultValue='587'>
                                                    <option value='25'>25</option>
                                                    <option value='465'>465</option>
                                                    <option value='587'>587</option>
                                                    <option value='2525'>2525</option>
                                                </Input>
                                            </Col>
                                        </Row><br></br>
                                        <Row><Input type='email' name='emailAddress' onChange={this.props.handleChange} value={this.props.emailAddress} placeholder='Username(usually your email address)'></Input></Row><br></br>
                                        <Row><Input type='password' name='smtpPassword' onChange={this.props.handleChange} value={this.props.smtpPassword} placeholder='Password'></Input></Row>
                                    </Col>
                                </Row><br></br>
                                <Row>
                                    <Col md={2}><i className="fas fa-inbox s-4"></i></Col>
                                    <Col md={10}>
                                        <Row>IMAP connection</Row>
                                        <Row><p style={{ fontSize: '0.7em' }}>This information comes from your email provider and is how we‘ll check your inbox for replies.</p></Row>
                                        <Row>
                                            <Col md={8}><Input onChange={this.props.handleChange} name='imapHost' value={this.props.imapHost} className='mt-4' type='text' placeholder='Host(e.g.mail.server.com)'></Input></Col>
                                            <Col md={4}><label className='selectbox_label' >Port Number</label>
                                                <Input type='select' name='imapPort' onChange={this.props.handleChange} defaultValue='993'>
                                                    <option value='143' >143</option>
                                                    <option value='993'>993</option>
                                                    <option value='995'>995</option>

                                                </Input>
                                            </Col>
                                        </Row><br></br>
                                        <Row><Input type='email' name='emailAddress' onChange={this.props.handleChange} value={this.props.emailAddress} placeholder='Username(usually your email address)'></Input></Row><br></br>
                                        <Row><Input type='password' name='imapPassword' onChange={this.props.handleChange} value={this.props.imapPassword} placeholder='Password'></Input></Row>
                                    </Col>
                                </Row>
                                <Row className='mt-4'>
                                    <Col md={2}><i className="fas fa-question s-4"></i></Col>
                                    <Col md={10}>
                                        <Row>Help</Row>
                                        <Row><p style={{ fontSize: '0.7em' }}>In most cases you‘ll need to contact your email provider or administrator to get help connecting your mail account. We‘re here to help as best we can.</p></Row>
                                        <Row><p style={{ fontSize: '0.7em' }}>Not having luck? Let Mailshake try auto-configuration.</p></Row><br></br>
                                    </Col>
                                </Row>
                            </Container>
                        </ModalBody>
                        <ModalFooter>
                            <Button type='submit' className="btn startBtn">NEXT<i className='fa fa-right-arrow '></i></Button>
                            <Button onClick={(e) => { e.preventDefault, this.setState({ modal: !this.props.modal }) }}>CANCEL</Button>
                        </ModalFooter>
                    </Form>
                </Modal>
            </div>
        )
    }
}

export default SmtpModal


