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
          window.location.href = 'Home.html';
        }
        render() {
          return (
            <div>
            <button type="button" class="btn-close" aria-label="Close" onClick={this.handleClick}></button>
            </div>
          )}};
class Search extends React.Component {
        handleClick = () => {
          window.location.href = 'InputGenerated.html';
        }
        render() {
          return (
            <nav className="navbar bg-body-tertiary">
              <div className="row container-fluid">
                <form className="d-flex" role="search">
                  <div className="input-group">
                    <input
                      className="form-control"
                      type="search"
                      placeholder="Search"
                      aria-label="Search"
                    />
                    <button className="btn btn-outline-success" type="button" onClick={this.handleClick}>
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-search" viewBox="0 0 16 16">
                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
                      </svg>
                    </button>
                  </div>
                </form>
              </div>
            </nav>
          )
        }
      };
class Filter extends React.Component {
        handleClick = () => {
        window.location.href = 'Filter.html';
      }
        render() {
            return (
            <div className="d-flex justify-content-end">
            <button className="btn" type="button"  onClick={this.handleClick}>
            <svg xmlns="http://www.w3.org/2000/svg" width={16} height={16} fill="darkgreen" className="bi bi-filter-right" viewBox="0 0 16 16">
                <path d="M14 10.5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 .5-.5zm0-3a.5.5 0 0 0-.5-.5h-7a.5.5 0 0 0 0 1h7a.5.5 0 0 0 .5-.5zm0-3a.5.5 0 0 0-.5-.5h-11a.5.5 0 0 0 0 1h11a.5.5 0 0 0 .5-.5z" />
            </svg>
            </button>
            </div>
    )}};
class ByCatagory extends React.Component {
    handleClick = () => {
        window.location.href = 'InputGenerated.html';
      }
    render()
     {
    return(
        <div>
        <div class="container text-center">
                <h3><b>New List </b></h3>
        <Search />
        <Filter />
        <div className="row row-cols-1 row-cols-md-2 g-4">
        <button className="btn" type="button">
        <div className="col">
        <div className="card text-bg-success mb-3" style={{ backgroundColor: "greenyellow ",maxWidth: "18rem" }}>
            <div class="card-header">Produce</div>
            
            <img src="https://i.imgur.com/UsGl0Ig.jpg" className="card-img-top" alt="Carrots, Tomato, Chard, Kale, Rasberries, and Nuts" />
            </div>
        </div>
        </button>
        <button className="btn" type="button"  onClick={this.handleClick} >
        <div className="col">
        <div className="card text-bg-success mb-3" style={{  backgroundColor: "greenyellow ",maxWidth: "18rem" }}>
            <div class="card-header">Dairy & Eggs</div>
            <img src="https://i.imgur.com/vKVvg13.jpg" className="card-img-top" alt="..." />
            </div>
        </div>
        </button>
        
        <button className="btn" type="button">
        <div className="col">
        <div className="card text-bg-success mb-3" style={{ backgroundColor: "greenyellow ", maxWidth: "18rem" }}>
            <div class="card-header">Beverages</div>
            <img src="https://i.imgur.com/XLRu30H.jpg" className="card-img-top" alt="..." />
            </div>
        </div>
        </button>
        <button className="btn" type="button">
        <div className="col">
            <div className="card text-bg-success mb-3" style={{ backgroundColor: "greenyellow ",maxWidth: "18rem" }}>
            <div class="card-header">Bakery</div>
            <img src="https://i.imgur.com/8vPafNx.jpg" className="card-img-top" alt="..." />
            </div>
        </div>
        </button>
        </div>
        <hr/>
        </div>
        </div>
      )}};
  
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
        <div className="card-body"style={{position: "absolute",top: "3rem"}}>
          <ByCatagory />           
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
    