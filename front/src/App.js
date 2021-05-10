// import logo from './logo.svg';
import './App.css';
import {useState} from 'react';


function App() {
  
  const [users, setUsers] = useState([{username: 'a'}, {username: 'b'}]);
  const [selectedTab, SelectTab] = useState(["abas-selecionada", "abas", "abas"]);

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
            <input className="search"></input>
            <div className="right-container">
                <div className="perfil-view">
                  <div className="user-name">Super Mario World</div>
                  <div className="follow-div">
                   <button className="follow-button-not-followed">Seguir</button>
                  </div>
                  <div className="follow-numbers-container">
                    <div className="follow-numbers">
                      <div className="follow">Seguindo: 1854</div>
                      <div className="follow">Seguidores: 50000</div>
                    </div>
                 </div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
