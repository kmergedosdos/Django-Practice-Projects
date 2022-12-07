import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Posts from './components/Posts';
import { useEffect, useState } from 'react';
import PostLoading from './components/PostLoading';


// const card = {
//   width: "300px",
//   backgroundColor: 'yellow',
//   display: 'flex',
//   flexDirection: 'column',
//   justifyContent: 'space-between'
// }


function App() {
  const [appState, setAppState] = useState({loading: false, posts: null})
  
  useEffect(() => {
    setAppState(prevState => ({...prevState, loading: true}));

    const apiUrl = "http://127.0.0.1:8000/api/";
    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => {
        setAppState({loading: false, posts: data});
      })
  }, []);

  return (
    <Router>
      <Header />
      {/* <Routes>
        <Route path='/' element={<Posts />}/>
      </Routes> */}
      <h1 style={{textAlign: 'center'}}>Latest Posts</h1>
      {
        appState.loading ? <PostLoading/> : <Posts postsData={appState.posts} />
      }
      {/* <div
        style={{
          display: "flex",
          gap: '1em'
        }}
      >
        <div style={card}>
          <p>Django Rest Framework Series - Part 1</p>
          <button style={{width: "fit-content"}}>Button</button>
        </div>
        <div style={card}>
        <p>Hello, and welcome to the first tutorial in this Django Rest Framework Series. In the following series of tutorials we will go through the Django Rest Framework and in addition build a React application to consume our Django Rest API. In this tutorial we work through a little bit of API theory then start to build a simple application in Django - based around a blog type of application. We move through the gears in Django then move across to React where we build an application to consume our new Django API.</p>
        <button style={{width: "fit-content"}}>Button</button>
        </div>
        <div style={card}>
        <p>learn Django - Towards Django Secure Deployment - Part-1</p>
        <button style={{width: "fit-content"}}>Button</button>
        </div>
      </div> */}
      <Footer />
    </Router>
  );
}

export default App;
