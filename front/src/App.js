// import logo from './logo.svg';
import './App.css';
import {useState} from 'react';

import UserView from './UserView';

function App() {
  
  const [users, setUsers] = useState([{username: 'a'}, {username: 'b'}]);
  const [selectedTab, SelectTab] = useState(["abas-selecionada", "abas", "abas"]);
  const [inputValue, setInputValue] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [userView, setUserView] = useState();

  const loadSearch = async (event) => {
    if (event.target.value === "") {
      setSearchResult([])
      return;
    };
    let data = ["a", "b"];
    setSearchResult(data);
  }

  const changeUserView = () => {
    let user = {
      name: "Sanic",
      followed: false,
      followedNumber: 20,
      followingNumber: 30
    }
    document.getElementsByClassName("search")[0].value = "";
    setSearchResult([]);
    setUserView(user);
  }

  return (
    <div className="app">
      <div className="header">NiceNetwork</div>
      <div className="app-body">
        <div className="part">
          <div className="box">
            <div className={selectedTab[0]}>Seguindo</div>
            <div className={selectedTab[1]}>Seguidores</div>
            <div className={selectedTab[2]}>Recom</div>
            <div className="perfis">
              {users.map((user) => 
                <div className="perfil" key={user.username}>
                  <div className="nome-perfil">{user.username}</div>
                  <button className="follow-button-not-followed">Seguir</button>
                </div>
              )}
              <div className="perfil">
                <div className="nome-perfil">UserName</div>
                <button className="follow-button-followed">Seguindo</button>
              </div>
            </div>
          </div>
        </div>
        <div className="part">
          <div className="box">
            <input className="search" onChange={loadSearch}></input>
            <div className="right-container">
              <div className="search-items">
                {searchResult.map((name) => 
                  <div className="search-item" onClick={() => changeUserView(name)}>{name}</div>
                )}
              </div>
              <UserView user={userView}/>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
