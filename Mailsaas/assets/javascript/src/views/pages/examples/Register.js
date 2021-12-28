/*!

=========================================================
* Argon Dashboard PRO React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-pro-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classnames from "classnames";
import axios from 'axios'
// reactstrap components
import {
  Button,
  Card,
  CardHeader,
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
} from "reactstrap";
// core components
import AuthHeader from "../../../components/Headers/AuthHeader"
import { connect } from "react-redux";
import { RegisterAction } from "../../../redux/action/AuthourizationAction";
import { Alert } from 'reactstrap';
class Register extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      FullName: '',
      Email: '',
      PhoneNumber: '',
      CompanyName: '',
      Password: '',
      mailsaas_type: 'Sales',
      isOpen: false,
      show: true,
      focusedName: false,
      focusedEmail: false,
      focusedPassword: false,
      focusedPhone: false,
      focusedCompany: false
    }

  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
    // this.setState({show:!this.state.show})
  }
  handleSubmit = (e) => {
    e.preventDefault();
    this.setState({ isOpen: false })

    const user = {
      full_name: this.state.FullName,
      email: this.state.Email,
      phone_number: this.state.PhoneNumber,
      company_name: this.state.CompanyName,
      password1: this.state.Password,
      mailsaas_type: this.state.mailsaas_type
    };

    this.props.RegisterAction(user)
  }
  render() {
    const { registerResponse, isRegisterSuccess } = this.props
    const { focusedName, focusedEmail, focusedPhone, focusedCompany, focusedPassword } = this.state
    return (
      <>
        <AuthHeader
          title="Create an account"
          lead="Use these awesome forms to login or create new account in your project for free."
        />
        <Container className="mt--8 pb-5" >
          <Row className="justify-content-center">
            <Col lg="6" md="8">
              <Card className="bg-secondary border-0">
                <CardBody className="px-lg-5 py-lg-2">
                  <div className="text-center text-muted mt-1 mb-4">
                    <small style={{ fontSize: 30, color: '#525f7f', fontWeight: 'bold' }}>Register</small>
                  </div>
                  <Form onSubmit={this.handleSubmit} role="form">
                    <FormGroup
                      className={classnames({
                        focused: focusedName
                      })}
                    >
                      <InputGroup className="input-group-merge input-group-alternative mb-3">
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="ni ni-hat-3" />
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input
                          placeholder="Name"
                          type="text"
                          name="FullName"
                          value={this.state.FullName}
                          onChange={this.handleChange}
                          onFocus={() => { this.setState({ focusedName: true }) }}
                          onBlur={() => { this.setState({ focusedName: false }) }}
                          autoComplete='off'
                          required
                        />
                      </InputGroup>
                    </FormGroup>
                    <FormGroup
                      className={classnames({
                        focused: focusedEmail
                      })}
                    >
                      <InputGroup className="input-group-merge input-group-alternative mb-3">
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="ni ni-email-83" />
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input
                          placeholder="Email"
                          type="email"
                          name='Email'
                          value={this.state.Email}
                          onChange={this.handleChange}
                          onFocus={() => this.setState({ focusedEmail: true })}
                          onBlur={() => this.setState({ focusedEmail: false })}
                          autoComplete='off'
                          required
                        />
                      </InputGroup>
                    </FormGroup>
                    {/*  */}
                    <FormGroup
                      className={classnames({
                        focused: focusedPhone
                      })}
                    >
                      <InputGroup className="input-group-merge input-group-alternative mb-3">
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="fa fa-phone" />
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input
                          placeholder="Phone Number"
                          type="number"
                          name='PhoneNumber'
                          onChange={this.handleChange}
                          onFocus={() => this.setState({ focusedPhone: true })}
                          onBlur={() => this.setState({ focusedPhone: false })}
                          required
                        />
                      </InputGroup>
                    </FormGroup>
                    <FormGroup
                      className={classnames({
                        focused: focusedCompany
                      })}
                    >
                      <InputGroup className="input-group-merge input-group-alternative mb-3">
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="fas fa-building" />
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input
                          placeholder="Comapany Name"
                          type="text"
                          name="CompanyName"
                          onChange={this.handleChange}
                          onFocus={() => this.setState({ focusedCompany: true })}
                          onBlur={() => this.setState({ focusedCompany: false })}
                          autoComplete='off'
                          required
                        />
                      </InputGroup>
                    </FormGroup>
                    {/*  */}
                    <FormGroup
                      className={classnames({
                        focused: focusedPassword
                      })}
                    >
                      <InputGroup className="input-group-merge input-group-alternative">
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="ni ni-lock-circle-open" />
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input
                          placeholder="Password"
                          type="password"
                          name="Password"
                          onClick={() => { this.setState({ show: !this.state.show }) }}
                          onChange={this.handleChange}
                          onFocus={() =>
                            this.setState({ focusedPassword: true })
                          }
                          onBlur={() =>
                            this.setState({ focusedPassword: false })
                          }
                          required
                        />
                      </InputGroup>
                      <div >
                        {!this.state.show && <span className='password-message'> A minimum 8 characters password contains a combination of uppercase and lowercase letter and number are required.</span>}
                      </div>
                      <FormGroup className='mt-4'>
                        <Input type="select" name="mailsaas_type" value={this.state.mailsaas_type} defaultValue='Sales' onChange={this.handleChange} id="exampleSelect">
                          <option value='Sales'>Sales</option>
                          <option value='Marketing'>Marketing/PR</option>
                          <option value='Recruiting'>Recruiting</option>
                          {/* <option value='other'>Other</option> */}
                        </Input>
                      </FormGroup>
                    </FormGroup>
                    {/* <div className="text-muted font-italic"> */}
                    {/* <small>
                        password strength:{" "}
                        <span className="text-success font-weight-700">
                          strong
                        </span>
                      </small> */}
                    {/* </div> */}
                    <Row className="my-4">
                      <Col xs="12">
                        <div className="custom-control custom-control-alternative custom-checkbox">
                          {/* <input
                            className="custom-control-input"
                            id="customCheckRegister"
                            type="checkbox"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor="customCheckRegister"
                          >
                            <span className="text-muted">
                              I agree with the{" "}
                              <a
                                href="#pablo"
                                onClick={e => e.preventDefault()}
                              >
                                Privacy Policy
                              </a>
                            </span>
                          </label> */}
                        </div>
                      </Col>
                    </Row>
                    <div className="text-center">
                      <Button className="mt-4 mb-4" color="info" type="submit" >
                        Create account
                      </Button>
                    </div>
                  </Form>
                  <Row>

                    {/* <div>
                      <p>{this.token}</p>
                    </div> */}
                  </Row>
                </CardBody>
              </Card>
            </Col>
          </Row>
        </Container>
        <div style={{ display: 'flex', justifyContent: 'center', position: 'fixed', bottom: 0, right: 0, left: 0 }}>
          <Alert className="alert_" toggle={() => {
            this.setState({ isOpen: true })
          }} isOpen={!this.state.isOpen && isRegisterSuccess} color="warning">{registerResponse}</Alert>
        </div>
      </>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    registerResponse: state.RegisterReducer.registerResponse,
    isRegisterSuccess: state.RegisterReducer.isRegisterSuccess
  };
};
const mapDispatchToProps = dispatch => ({
  RegisterAction: user => { dispatch(RegisterAction(user)); },
});
export default connect(mapStateToProps, mapDispatchToProps)(Register);
