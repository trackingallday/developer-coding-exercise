import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import PostsList from "./PostsList";
import Post from './Post'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PostsList />} />
        <Route path="/post/:slug" element={<Post />} />
      </Routes>
    </Router>
  );
}

export default App;
