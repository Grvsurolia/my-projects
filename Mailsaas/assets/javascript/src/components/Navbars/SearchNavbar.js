import React, { Component } from 'react'
import {
    Collapse,
    DropdownMenu,
    DropdownItem,
    UncontrolledDropdown,
    DropdownToggle,
    Form,
    Navbar,
    Media,
    FormGroup,
    NavItem,
    Input,
    InputGroupAddon,
    InputGroupText,
    InputGroup,
    ListGroupItem,
    Nav,
    Container,
} from "reactstrap";
import classnames from "classnames";

export default class SearchNavbar extends Component {
    openSearch = () => {
        document.body.classList.add("g-navbar-search-showing");
        setTimeout(function () {
            document.body.classList.remove("g-navbar-search-showing");
            document.body.classList.add("g-navbar-search-show");
        }, 150);
        setTimeout(function () {
            document.body.classList.add("g-navbar-search-shown");
        }, 300);
    };
    // function that on mobile devices makes the search close
    closeSearch = () => {
        document.body.classList.remove("g-navbar-search-shown");
        setTimeout(function () {
            document.body.classList.remove("g-navbar-search-show");
            document.body.classList.add("g-navbar-search-hiding");
        }, 150);
        setTimeout(function () {
            document.body.classList.remove("g-navbar-search-hiding");
            document.body.classList.add("g-navbar-search-hidden");
        }, 300);
        setTimeout(function () {
            document.body.classList.remove("g-navbar-search-hidden");
        }, 500);
    };
    render() {
        return (
            <div>
                <Navbar style={{border:'2px solid',background:'#11cdef'}}
                    className={classnames(
                        "navbar-top navbar-expand border-bottom",
                        { "navbar-dark bg-info": this.props.theme === "dark" },
                        { "navbar-light bg-secondary": this.props.theme === "light" }
                    )}
                >
                    <Container fluid >
                        <Collapse navbar isOpen={true}>
                            <Form
                                className={classnames(
                                    "navbar-search form-inline mr-sm-3",
                                    { "navbar-search-light": this.props.theme === "dark" },
                                    { "navbar-search-dark": this.props.theme === "light" }
                                )}
                            >
                                <FormGroup className="mb-0" >
                                    <InputGroup className="input-group-alternative input-group-merge">
                                        <InputGroupAddon addonType="prepend">
                                            <InputGroupText>
                                                <i className="fas fa-search" />
                                            </InputGroupText>
                                        </InputGroupAddon>
                                        <Input placeholder="Search" type="text" />
                                    </InputGroup>
                                </FormGroup>
                                <button
                                    aria-label="Close"
                                    className="close"
                                    type="button"
                                    onClick={this.closeSearch}
                                >
                                    <span aria-hidden={true}>×</span>
                                </button>
                            </Form>
                            <Nav className="align-items-center ml-auto ml-md-0" navbar>
                                <UncontrolledDropdown nav>
                                    <DropdownToggle className="nav-link pr-0" color="" tag="a">
                                        <Media className="align-items-center">
                                            <span className="avatar avatar-sm rounded-circle">
                                                <img
                                                    alt="..."
                                                    src={STATIC_FILES.team_4}
                                                />
                                            </span>
                                            <Media className="ml-2 d-none d-lg-block">
                                                <span className="mb-0 text-sm font-weight-bold">
                                                    John Snow
                        </span>
                                            </Media>
                                        </Media>
                                    </DropdownToggle>
                                    <DropdownMenu right>
                                        <DropdownItem className="noti-title" header tag="div">
                                            <h6 className="text-overflow m-0">Welcome!</h6>
                                        </DropdownItem>
                                        <DropdownItem
                                            href="#pablo"
                                            onClick={e => e.preventDefault()}
                                        >
                                            <i className="ni ni-single-02" />
                                            <span>My profile</span>
                                        </DropdownItem>
                                        <DropdownItem
                                            href="#pablo"
                                            onClick={e => e.preventDefault()}
                                        >
                                            <i className="ni ni-settings-gear-65" />
                                            <span>Settings</span>
                                        </DropdownItem>
                                        <DropdownItem divider />
                                        <DropdownItem
                                            href="#pablo"
                                            onClick={e => e.preventDefault()}
                                        >
                                            <i className="ni ni-user-run" />
                                            <span>Logout</span>
                                        </DropdownItem>
                                    </DropdownMenu>
                                </UncontrolledDropdown>
                            </Nav>
                        </Collapse>
                    </Container>
                </Navbar>
            </div>
        )
    }
}
