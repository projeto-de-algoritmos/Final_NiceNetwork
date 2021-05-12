// import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';

import UserView from './UserView';

import api from './api';

function App() {
  const [currentUser, setCurrentUser] = useState({name: ""});
  const [users, setUsers] = useState([]);
  const [selectedTab, SelectTab] = useState([
    {class: "abas-selecionada", label: "Seguindo"},
    {class: "abas", label: "Seguidores"},
    {class: "abas", label: "Recomendados"}
  ]);
  const [searchResult, setSearchResult] = useState([]);
  const [userView, setUserView] = useState();
  const [inicialLoading, setInicialLoading] = useState(true);

  useEffect(() => {
    (async function () {
      if (inicialLoading === true) {
        let response = await api.get(`currentuser`)
        let user = response.data;
        response = await api.get(`following/${user}`);
        setCurrentUser({name: user});
        setUsers(response.data);
        await setInicialLoading(false);
      }
    })()
  }, [inicialLoading])

  // useEffect( () => {
  //   changeTab(0);
  // }, [currentUser])

  const loadSearch = async (event) => {
    if (event.target.value === "") {
      setSearchResult([])
      return;
    };
    let response = await api.get(`search/${event.target.value}`);
    setSearchResult(response.data);
  }

  const updateTab = (user) => {
    let i;
    for (i in selectedTab) {
      if (selectedTab[i].class === "abas-selecionada") break;
    }
    getUsers(i, user);
  }

  const getUsers = async (i, user) => {
    if (user == undefined) {
      user = currentUser.name;
    }
    let userlist = [], response;
    switch (Number(i)) {
      case 0: //seguindo
        response = await api.get(`following/${user}`);
        userlist = response.data;
        break;
      case 1: //seguidores
        userlist = [{username: 'c'}, {username: 'd'}]
        break;
      case 2: //recomendados
        response = await api.get(`recom`);
        userlist = response.data;
        break;
    }
    setUsers(userlist);
  }

  const changeTab = (i) => {
    let select = [];
    for (let j = 0; j < selectedTab.length; j++) {
      if (j === i) {
        select.push({class: "abas-selecionada", label: selectedTab[j].label})
      }
      else {
        select.push({class: "abas", label: selectedTab[j].label})
      }
    }
    SelectTab(select);
    getUsers(i);
  }

  const changeUser = async () => {
    let user = prompt("Escreva o nome do usuário:");
    if (user.search(/^[a-zA-Z]+$/i) == -1) {
      //TODO melhorar este feedback
      alert("Favor, utilizar apenas letras");
      return;
    }
    await api.get(`change/${user}`);
    updateTab(user);
    setCurrentUser({name: user});
  }

  const changeUserView = async (name) => {
    try {
      let user = await api.get(`/user/${name}`)
      document.getElementsByClassName("search")[0].value = "";
      setSearchResult([]);
      setUserView(user.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="app">
      <div className="header">NiceNetwork</div>
      <div className="current-user-change" onClick={changeUser}>Trocar usuário<br/>{currentUser.name}</div>
      <div className="app-body">
        <div className="part">
          <div className="box">
            {selectedTab.map((selected, i) => 
              <div className={selected.class} key={selected.label} onClick={() => changeTab(i)}>{selected.label}</div>
            )}
            <div className="perfis">
              {users.map((user) => 
                <div className="perfil" key={user} onClick={() => changeUserView(user)}>
                  <div className="nome-perfil">{user}</div>
                  {/* <button className="follow-button-not-followed">Seguir</button> */}
                </div>
              )}
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
              <UserView user={userView} callback={changeUserView} update={updateTab}/>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
