import React, { Component } from 'react'
import classnames from "classnames";
import {
    CardBody,
    FormGroup,
    Form,
    Input,
    InputGroupAddon,
    InputGroupText,
    InputGroup,
    Container,
    Row,
    Col,
    Button,
    Card,
} from 'reactstrap'
import AuthHeader from "../../../components/Headers/AuthHeader.js";

export default class ForgetPassword extends Component {
    constructor(props) {
        super(props)
        this.state = {
            oldPassword: '',
            newPassword: '',
            focusedEmail: false,
            focusedPassword: false
        }
    }
    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    handleSubmit = (e) => {
        e.preventDefault();
        console.log('forgot===>',this.state)
    }
    render() {
        return (
            <>
                <AuthHeader
                    title="Reset Password"
                    lead=""
                />
                <Container className="mt--8 pb-5">
                    <Row className="justify-content-center">
                        <Col lg="6" md="7">
                            <Card className="bg-secondary border-0 mb-0">
                                <CardBody className="px-lg-5 py-lg-5">
                                    <Form onSubmit={this.handleSubmit} role="form">
                                        <FormGroup
                                            className={classnames("mb-3", {
                                                focused: this.state.focusedEmail
                                            })}
                                        >
                                            <InputGroup className="input-group-merge input-group-alternative">
                                                <InputGroupAddon addonType="prepend">
                                                    <InputGroupText>
                                                        <i className="ni ni-lock-circle-open" />
                                                    </InputGroupText>
                                                </InputGroupAddon>
                                                <Input
                                                    placeholder="Old Password"
                                                    type="password"
                                                    name="oldPassword"
                                                    onChange={this.handleChange}
                                                    value={this.state.email}
                                                    onFocus={() => this.setState({ focusedEmail: true })}
                                                    onBlur={() => this.setState({ focusedEmail: false })}
                                                    autoComplete='off'
                                                />
                                            </InputGroup>
                                        </FormGroup>
                                        <FormGroup
                                            className={classnames({
                                                focused: this.state.focusedPassword
                                            })}
                                        >
                                            <InputGroup className="input-group-merge input-group-alternative">
                                                <InputGroupAddon addonType="prepend">
                                                    <InputGroupText>
                                                        <i className="ni ni-lock-circle-open" />
                                                    </InputGroupText>
                                                </InputGroupAddon>
                                                <Input
                                                    placeholder="New Password"
                                                    type="password"
                                                    name="newPassword"
                                                    onChange={this.handleChange}
                                                    value={this.state.password}
                                                    onFocus={() =>
                                                        this.setState({ focusedPassword: true })
                                                    }
                                                    onBlur={() =>
                                                        this.setState({ focusedPassword: false })
                                                    }
                                                />
                                            </InputGroup>
                                        </FormGroup>
                                        <div className="text-center">
                                            <Button className="my-4" color="info" type="submit">Reset password</Button>
                                        </div>
                                    </Form>
                                </CardBody>
                            </Card>
                        </Col>
                    </Row>
                </Container>
            </>
        )
    }
}
