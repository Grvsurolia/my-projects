import React, { Component } from 'react'
import { Button, Container, Modal, ModalHeader, ModalBody, ModalFooter, Row, Col, Form, Input } from 'reactstrap';
import { connect } from "react-redux";

class UnsubscribesModal extends Component {
    constructor(props) {
        super(props)
    }
    render() {
        const { unsubscribeWithEmail,unsubscribeWithCsv,handleSubmit,loading} = this.props;
        console.log(loading)
        return (
            <div className="unsbuscribe-modal">
                <Modal isOpen={this.props.isOpen}>
                    <Form handleSubmit={handleSubmit}>
                        <ModalHeader toggle={this.props.toggle}><h1 className="unsubscribe-modal-title">Unsubscribe email addresses </h1><p className="example-text"><strong>TIP:</strong> Block a whole domain like this: *@example.com</p></ModalHeader>
                        {loading ?<div className="loader"></div>
                            : <ModalBody >
                                <Container className="unsubscribe_container" >
                                    <Row>
                                        <Col md='5'>
                                            <textarea onChange={unsubscribeWithEmail} placeholder='Email addresses' required></textarea>
                                        </Col>
                                        <Col md='1'>or</Col>
                                        <Col md='6'>Upload a CSV (comma-separated-values) file up to 1MB. It should contain just one column or have a column with the word "email" in it.</Col>
                                    </Row>
                                    <Row>
                                        <div className="unsubscribe-btn-wrapper" >
                                            <button className='btn choose_file'>Submit</button>
                                        </div>
                                        <div style={{ width: '60%' }} className="unsubscribe-btn-wrapper" >
                                            <Input onChange={unsubscribeWithCsv} type='file' name='csvFile' className="choose_file btn chooseOption"></Input>
                                        </div>
                                    </Row>
                                </Container>
                            </ModalBody>}
                        <ModalFooter>
                            <Button onClick={(e) => { e.preventDefault(); this.props.handleClose() }}>CANCEL</Button>
                        </ModalFooter>
                    </Form>
                </Modal>
            </div>
        )
    }
}
export default UnsubscribesModal;