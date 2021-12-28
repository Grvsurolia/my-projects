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
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { createStore } from 'redux'
// react library for routing
import { Router, Route, Switch, Redirect } from "react-router-dom";


import "react-notification-alert/dist/animate.css";
import "react-perfect-scrollbar/dist/css/styles.css";
import "@fullcalendar/common/main.min.css";
import "@fullcalendar/daygrid/main.min.css";
import "sweetalert2/dist/sweetalert2.min.css";
import "select2/dist/css/select2.min.css";
import "quill/dist/quill.core.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

// bootstrap rtl for rtl support page
// // import "./assets/vendor/bootstrap-rtl/bootstrap-rtl.scss";
// // plugins styles from node_modules
// import "react-notification-alert/dist/animate.css";
// import "react-perfect-scrollbar/dist/css/styles.css";
// // plugins styles downloaded
// import "./assets/vendor/fullcalendar/dist/fullcalendar.min.css";
// import "./assets/vendor/sweetalert2/dist/sweetalert2.min.css";
// import "./assets/vendor/select2/dist/css/select2.min.css";
// import "./assets/vendor/quill/dist/quill.core.css";
// import "./assets/vendor/nucleo/css/nucleo.css";
// import "./assets/vendor/@fortawesome/fontawesome-free/css/all.min.css";
// // core styles
// import "./assets/scss/argon-dashboard-pro-react.scss?v1.1.0";
import "./assets/vendor/nucleo/css/nucleo.css";
import "./assets/scss/argon-dashboard-pro-react.scss?v1.2.0";

// import RTLLayout from "layouts/RTL.js";
// import AuthLayout from "layouts/Auth.js";
import AdminLayout from "./layouts/Admin"
import AuthLayout from "./layouts/Auth"
import IndexView from "./views/Index.js";
import store from './redux/store/store'
import { createBrowserHistory } from 'history'
export const history = createBrowserHistory()
ReactDOM.render(
  <Router history={history}>
    <Provider store={store}>
      <Switch>
        <Route path="/app/admin" render={props => <AdminLayout {...props} />} />
        <Route path="/app/auth" render={props => <AuthLayout {...props} />} />
        <Route path="/app" render={props => <IndexView {...props} />} />
      </Switch>
    </Provider>
  </Router>,
  document.getElementById("object-lifecycle-home")
  

);
