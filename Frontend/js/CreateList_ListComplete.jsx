class Profile extends React.Component {
    handleClick = () => {
        window.location.href = 'Profile.html';
      }
    render() {
      return (
      <div>
        <button className="btn" type="button"  onClick={this.handleClick}>
        <svg xmlns="http://www.w3.org/2000/svg" width={36} height={36} fill="darkgreen" className="bi bi-person-circle" viewBox="0 0 16 16" >
        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" /> 
        <path fillRule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
        </svg>
        </button>
      </div>
      )}};
class Exit extends React.Component {
        handleClick = () => {
            window.location.href = 'InputGenerated.html';
        }
        render() {
            return (
              <div>
                <button type="button" class="btn-close" aria-label="Close" onClick={this.handleClick}></button>
              </div>
            )}};
class ListComplete extends React.Component {
  render() {
    return (
      <div class="container text-center" style={{ marginTop: "3rem" }}>
          <h1 class="display-6">Successfully added item to list! </h1>
          <div className="card-body">
          <h6 className="card-title"><b>Current List: Aldi</b></h6>
              <ul className="list-group list-group-flush">
              <li className="list-group-item d-flex" style={{ height: "100px" }}>
                  <div className="flex-grow-1">
                      <img
                      src="https://i.imgur.com/92G0iMF.jpg"
                      className="img-fluid rounded-start"
                      alt="..."
                      style={{ maxWidth: "90px" }}
                      />
                  </div>
                  <div className="ms-3">
                      $2.65 L'oven Fresh 100% Whole Wheat Bread 
                  </div>
              </li>
              <li className="list-group-item d-flex" style={{ height: "100px" }}>
                  <div className="flex-grow-1">
                      <img
                      src="https://i.imgur.com/DKKCrQa.jpg"
                      className="img-fluid rounded-start"
                      alt="..."
                      style={{ maxWidth: "90px" }}
                      />
                  </div>
                  <div className="ms-3">
                      $5.49 Oreo Chocolate Sandwich Cookies
                  </div>
              </li>
              <li className="list-group-item d-flex" style={{ height: "100px" }}>
                  <div className="flex-grow-1">
                      <img
                      src="https://i.imgur.com/agRrKtx.jpg"
                      className="img-fluid rounded-start"
                      alt="..."
                      style={{ maxWidth: "90px" }}
                      />
                  </div>
                  <div className="ms-3">
                    $2.55 Goldhen Grade A Large Eggs
                  </div>
              </li>
              </ul>
              <p className="card-text">
              <div>
            <button type="button" class="btn btn-success">Complete List</button>               
            </div>
              </p>
          </div>
      </div>
    )
  }
};


class Frame extends React.Component {
  render() {
    return (
      <div className="card" style={{
        backgroundColor: "white",
        border: "6px solid black",
        overflow: "hidden",
        borderRadius: 15,
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
        height: "36rem",
        width: "24rem",
        padding: "0.5rem",
        position: "relative"
      }}>
        <div style={{
          position: "absolute",
          top: "0.5rem",
          left: "0.5rem"
        }}>
          <Profile />
        </div>
        <div style={{
          position: "absolute",
          top: "0.5rem",
          right: "0.5rem"
        }}>
          <Exit />
        </div>
        <div className="card-body"style={{position: "absolute",top: "1rem"}}>
          <ListComplete />           
        </div>
      </div>
    );
  }
}

  
ReactDOM.render(
  <div style={{
    display: "flex",
    height: "1180px",
    justifyContent: "center",
    alignItems: "center"}}>
  <Frame />
</div>, 
document.getElementById('root')
);