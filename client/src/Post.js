import React, { useEffect, useState } from 'react';
import {
  useParams,
} from "react-router-dom";
import ReactMarkdown from 'react-markdown'



export default function Post(props) {

  const [post, setPost] = useState({});
  const { slug } = useParams();

  useEffect(() => {
    // this should be a dot-env var
    fetch('http://127.0.0.1:3000/posts/' + slug + '/').then(res => res.json()).then(data => setPost(data));
  }, []);

  if(!post.content) return (<div>Loading...</div>);

  return (<div>
    <ReactMarkdown>{ post.content }</ReactMarkdown>
    <h3>Tags</h3>
    <div>
      { post.tags.map((t, i) => <span key={i}><b>{t}, </b></span>)}
    </div>
  </div>)

}