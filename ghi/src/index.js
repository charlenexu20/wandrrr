import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
// import reportWebVitals from './reportWebVitals';
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// async function loadData () {
//   const userResponse = await fetch('http://localhost:8000/token/');


//   if (userResponse.ok) {
//     const userData = await userResponse.json();
//     root.render(
//       <React.StrictMode>
//         <App user={userData.account} />
//       </React.StrictMode>
//     );
//   } else {
//     console.error(userResponse);


//   }
// }
// loadData();




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
