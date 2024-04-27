var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Profile = function (_React$Component) {
  _inherits(Profile, _React$Component);

  function Profile() {
    var _ref;

    var _temp, _this, _ret;

    _classCallCheck(this, Profile);

    for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    return _ret = (_temp = (_this = _possibleConstructorReturn(this, (_ref = Profile.__proto__ || Object.getPrototypeOf(Profile)).call.apply(_ref, [this].concat(args))), _this), _this.handleClick = function () {
      window.location.href = 'Profile.html';
    }, _temp), _possibleConstructorReturn(_this, _ret);
  }

  _createClass(Profile, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "button",
          { className: "btn", type: "button", onClick: this.handleClick },
          React.createElement(
            "svg",
            { xmlns: "http://www.w3.org/2000/svg", width: 36, height: 36, fill: "darkgreen", className: "bi bi-person-circle", viewBox: "0 0 16 16" },
            React.createElement("path", { d: "M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" }),
            React.createElement("path", { fillRule: "evenodd", d: "M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z" })
          )
        )
      );
    }
  }]);

  return Profile;
}(React.Component);

;

var Exit = function (_React$Component2) {
  _inherits(Exit, _React$Component2);

  function Exit() {
    var _ref2;

    var _temp2, _this2, _ret2;

    _classCallCheck(this, Exit);

    for (var _len2 = arguments.length, args = Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
      args[_key2] = arguments[_key2];
    }

    return _ret2 = (_temp2 = (_this2 = _possibleConstructorReturn(this, (_ref2 = Exit.__proto__ || Object.getPrototypeOf(Exit)).call.apply(_ref2, [this].concat(args))), _this2), _this2.handleClick = function () {
      window.location.href = 'InputGenerated.html';
    }, _temp2), _possibleConstructorReturn(_this2, _ret2);
  }

  _createClass(Exit, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement("button", { type: "button", "class": "btn-close", "aria-label": "Close", onClick: this.handleClick })
      );
    }
  }]);

  return Exit;
}(React.Component);

;

var ListComplete = function (_React$Component3) {
  _inherits(ListComplete, _React$Component3);

  function ListComplete() {
    _classCallCheck(this, ListComplete);

    return _possibleConstructorReturn(this, (ListComplete.__proto__ || Object.getPrototypeOf(ListComplete)).apply(this, arguments));
  }

  _createClass(ListComplete, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        { "class": "container text-center", style: { marginTop: "3rem" } },
        React.createElement(
          "h1",
          { "class": "display-6" },
          "Successfully added item to list! "
        ),
        React.createElement(
          "div",
          { className: "card-body" },
          React.createElement(
            "h6",
            { className: "card-title" },
            React.createElement(
              "b",
              null,
              "Current List: Aldi"
            )
          ),
          React.createElement(
            "ul",
            { className: "list-group list-group-flush" },
            React.createElement(
              "li",
              { className: "list-group-item d-flex", style: { height: "100px" } },
              React.createElement(
                "div",
                { className: "flex-grow-1" },
                React.createElement("img", {
                  src: "https://i.imgur.com/92G0iMF.jpg",
                  className: "img-fluid rounded-start",
                  alt: "...",
                  style: { maxWidth: "90px" }
                })
              ),
              React.createElement(
                "div",
                { className: "ms-3" },
                "$2.65 L'oven Fresh 100% Whole Wheat Bread"
              )
            ),
            React.createElement(
              "li",
              { className: "list-group-item d-flex", style: { height: "100px" } },
              React.createElement(
                "div",
                { className: "flex-grow-1" },
                React.createElement("img", {
                  src: "https://i.imgur.com/DKKCrQa.jpg",
                  className: "img-fluid rounded-start",
                  alt: "...",
                  style: { maxWidth: "90px" }
                })
              ),
              React.createElement(
                "div",
                { className: "ms-3" },
                "$5.49 Oreo Chocolate Sandwich Cookies"
              )
            ),
            React.createElement(
              "li",
              { className: "list-group-item d-flex", style: { height: "100px" } },
              React.createElement(
                "div",
                { className: "flex-grow-1" },
                React.createElement("img", {
                  src: "https://i.imgur.com/agRrKtx.jpg",
                  className: "img-fluid rounded-start",
                  alt: "...",
                  style: { maxWidth: "90px" }
                })
              ),
              React.createElement(
                "div",
                { className: "ms-3" },
                "$2.55 Goldhen Grade A Large Eggs"
              )
            )
          ),
          React.createElement(
            "p",
            { className: "card-text" },
            React.createElement(
              "div",
              null,
              React.createElement(
                "button",
                { type: "button", "class": "btn btn-success" },
                "Complete List"
              )
            )
          )
        )
      );
    }
  }]);

  return ListComplete;
}(React.Component);

;

var Frame = function (_React$Component4) {
  _inherits(Frame, _React$Component4);

  function Frame() {
    _classCallCheck(this, Frame);

    return _possibleConstructorReturn(this, (Frame.__proto__ || Object.getPrototypeOf(Frame)).apply(this, arguments));
  }

  _createClass(Frame, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        { className: "card", style: {
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
          } },
        React.createElement(
          "div",
          { style: {
              position: "absolute",
              top: "0.5rem",
              left: "0.5rem"
            } },
          React.createElement(Profile, null)
        ),
        React.createElement(
          "div",
          { style: {
              position: "absolute",
              top: "0.5rem",
              right: "0.5rem"
            } },
          React.createElement(Exit, null)
        ),
        React.createElement(
          "div",
          { className: "card-body", style: { position: "absolute", top: "1rem" } },
          React.createElement(ListComplete, null)
        )
      );
    }
  }]);

  return Frame;
}(React.Component);

ReactDOM.render(React.createElement(
  "div",
  { style: {
      display: "flex",
      height: "1180px",
      justifyContent: "center",
      alignItems: "center" } },
  React.createElement(Frame, null)
), document.getElementById('root'));