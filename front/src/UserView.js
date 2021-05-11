function UserView({user}) {

	if (user == undefined) {
		user = {
			name: "Super Mario World",
			followed: true,
			followedNumber: 10,
			followingNumber: 5000
		}
	}

	let followButton = <button className="follow-button-not-followed">Seguir</button>;
	if (user.followed)
		followButton = <button className="follow-button-followed">Seguindo</button>;

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