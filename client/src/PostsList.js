import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export default function PostsList(props) {

  const [posts, setPosts] = useState([])

  useEffect(() => {
    // again should be in dotenv vars
    fetch('http://127.0.0.1:3000/').then(res => res.json()).then(data => setPosts(data));
  }, []);

  return (<div>
    <h1>Posts</h1>

    <ul>
    
      { posts.map(post => <li key={post.slug}><Link to={`/post/${post.slug}`}>{post.title}</Link></li>) }
    
    </ul>
  
  </div>)

}