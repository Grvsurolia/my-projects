import React, { Component } from 'react'
import "../css/main.css"
import { Button, Modal, Form } from 'react-bootstrap';
import axios from 'axios';
import { ReactComponent as Delete } from "../Asset/delete.svg";
import { API_URL } from '../Constants';

export default class SMTP extends Component {
    constructor() {
        super();
        this.state = {
            show: false,
            username: '',
            password: '',
            host: '',
            port: '',
            accounts: []
        }
    }
    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    handleSubmit = (e) => {
        e.preventDefault();
        this.setState({
            show: false,
        })
        
        axios.post(`${API_URL}/mail/account/`, {
            smtp_username: this.state.username,
            smtp_password: this.state.password,
            smtp_host: this.state.host,
            smtp_port: this.state.port
        })
            .then((response) => {
                const msg = response.data.sucess;
                if (msg === false) {
                    alert(response.data.message)
                }
                else {
                    this.getApi();
                }
            })
            .catch(error => {
                console.error('There was an error!', error);
            })
    }
    getApi = () => {
        axios.get(`${API_URL}/mail/account/`)
            .then((response) => {
                return this.setState({ accounts: response.data.data })
            })
            .catch(error => {
                console.error('There was an error!', error);
            })
    }
    
    componentDidMount() {
        this.getApi();
    }

    handleDelete = (id) => {
        axios.delete(`${API_URL}/mail/account/${id}`)
            .then((response) => {
                this.getApi()
            })
            .catch(error => {
                console.error('There was an error!', error);
            })
    }

    render() {
        const { show, accounts } = this.state;
        return (
            <div>
                <h3>List of connected Accounts</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <th>User Name</th>
                            <th>Email</th>
                            <th>Host Name</th>
                            <th>Port Name</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {accounts.map((item, index) => {
                            return <tr key={index}>
                                <td>{item.smtp_username}</td>
                                <td>{item.smtp_username}</td>
                                <td>{item.smtp_host}</td>
                                <td>{item.smtp_port}</td>
                                <td style={{cursor: 'pointer'}}>
                                    <span onClick={()=>this.handleDelete(item.id)}>
                                        <Delete />
                                    </span>
                                </td>
                            </tr>
                        })}
                    </tbody>
                </table>
                <Modal show={show} backdrop="static" keyboard={false}>
                    <Form onSubmit={this.handleSubmit}>
                        <Modal.Header ><Modal.Title>SMTP <span className='float-right' onClick={() => { this.setState({ show: false }) }} >&#10006;</span></Modal.Title></Modal.Header>
                        <Modal.Body>
                            <label>Email : </label>
                            <input type='email' className='form-control' name='username' value={this.state.user} onChange={this.handleChange} required></input><br></br>
                            <label>Password : </label>
                            <input type='password' className='form-control' name='password' value={this.state.password} onChange={this.handleChange} required></input><br></br>
                            <label>Host Name : </label>
                            <input type='text' className='form-control' name='host' value={this.state.host} onChange={this.handleChange} required></input><br></br>
                            <label>Port Name : </label>
                            <input type='number' className='form-control' name='port' value={this.state.port} onChange={this.handleChange} required></input><br></br>
                        </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={() => { this.setState({ show: false }) }} >Close</Button>
                            <Button variant="primary" type='submit'> Add</Button>
                        </Modal.Footer>
                    </Form>
                </Modal>

                <Button className='add' onClick={() => { this.setState({ show: true }) }}>Add Account</Button>
            </div>
        )
    }
}