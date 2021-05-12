import api from './api';

function UserView({user, callback, update}) {

	if (user == undefined) {
		return (
			<div className="perfil-view"></div>
		)
	}

	const follow = async () => {
		await api.get(`follow/${user.name}`);
		callback(user.name);
		update();
	}

	const unfollow = async () => {
		await api.get(`unfollow/${user.name}`);
		callback(user.name);
		update();
	}

	const buttons = [
		<button className="follow-button-not-followed" onClick={follow}>Seguir</button>,
		<button className="follow-button-followed" onClick={unfollow}>Seguindo</button>
	]

	let followButton = buttons[0];

	if (user.followedByCurrentUser)
		followButton = buttons[1];

	return (
		<div className="perfil-view">
			<div className="user-name">{user.name}</div>
			<div className="follow-div">
				{followButton}
			</div>
			<div className="follow-numbers-container">
				<div className="follow-numbers">
					<div className="follow">Seguindo: {user.followingNumber}</div>
					<div className="follow">Seguidores: {user.followedNumber}</div>
				</div>
			</div>
		</div>
	);

}

export default UserView;