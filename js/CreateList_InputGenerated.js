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
      window.location.href = 'Catagories.html';
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

var Filter = function (_React$Component3) {
  _inherits(Filter, _React$Component3);

  function Filter() {
    var _ref3;

    var _temp3, _this3, _ret3;

    _classCallCheck(this, Filter);

    for (var _len3 = arguments.length, args = Array(_len3), _key3 = 0; _key3 < _len3; _key3++) {
      args[_key3] = arguments[_key3];
    }

    return _ret3 = (_temp3 = (_this3 = _possibleConstructorReturn(this, (_ref3 = Filter.__proto__ || Object.getPrototypeOf(Filter)).call.apply(_ref3, [this].concat(args))), _this3), _this3.handleClick = function () {
      window.location.href = 'Filter.html';
    }, _temp3), _possibleConstructorReturn(_this3, _ret3);
  }

  _createClass(Filter, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        { className: "d-flex justify-content-end" },
        React.createElement(
          "button",
          { className: "btn", type: "button", onClick: this.handleClick },
          React.createElement(
            "svg",
            { xmlns: "http://www.w3.org/2000/svg", width: 16, height: 16, fill: "darkgreen", className: "bi bi-filter-right", viewBox: "0 0 16 16" },
            React.createElement("path", { d: "M14 10.5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 .5-.5zm0-3a.5.5 0 0 0-.5-.5h-7a.5.5 0 0 0 0 1h7a.5.5 0 0 0 .5-.5zm0-3a.5.5 0 0 0-.5-.5h-11a.5.5 0 0 0 0 1h11a.5.5 0 0 0 .5-.5z" })
          )
        )
      );
    }
  }]);

  return Filter;
}(React.Component);

;

var NextPage = function (_React$Component4) {
  _inherits(NextPage, _React$Component4);

  function NextPage() {
    var _ref4;

    var _temp4, _this4, _ret4;

    _classCallCheck(this, NextPage);

    for (var _len4 = arguments.length, args = Array(_len4), _key4 = 0; _key4 < _len4; _key4++) {
      args[_key4] = arguments[_key4];
    }

    return _ret4 = (_temp4 = (_this4 = _possibleConstructorReturn(this, (_ref4 = NextPage.__proto__ || Object.getPrototypeOf(NextPage)).call.apply(_ref4, [this].concat(args))), _this4), _this4.handleClick = function () {
      window.location.href = 'ListComplete.html';
    }, _temp4), _possibleConstructorReturn(_this4, _ret4);
  }

  _createClass(NextPage, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "button",
          { type: "button", "class": "btn btn-success", onClick: this.handleClick },
          "Add to List"
        )
      );
    }
  }]);

  return NextPage;
}(React.Component);

;

var Search = function (_React$Component5) {
  _inherits(Search, _React$Component5);

  function Search() {
    var _ref5;

    var _temp5, _this5, _ret5;

    _classCallCheck(this, Search);

    for (var _len5 = arguments.length, args = Array(_len5), _key5 = 0; _key5 < _len5; _key5++) {
      args[_key5] = arguments[_key5];
    }

    return _ret5 = (_temp5 = (_this5 = _possibleConstructorReturn(this, (_ref5 = Search.__proto__ || Object.getPrototypeOf(Search)).call.apply(_ref5, [this].concat(args))), _this5), _this5.handleClick = function () {
      window.location.href = 'InputGenerated.html';
    }, _temp5), _possibleConstructorReturn(_this5, _ret5);
  }

  _createClass(Search, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "nav",
        { className: "navbar bg-body-tertiary" },
        React.createElement(
          "div",
          { className: "row container-fluid" },
          React.createElement(
            "form",
            { className: "d-flex", role: "search" },
            React.createElement(
              "div",
              { className: "input-group" },
              React.createElement("input", {
                className: "form-control",
                type: "search",
                placeholder: "Search",
                "aria-label": "Search"
              }),
              React.createElement(
                "button",
                { className: "btn btn-outline-success", type: "button", onClick: this.handleClick },
                React.createElement(
                  "svg",
                  { xmlns: "http://www.w3.org/2000/svg", width: "16", height: "16", fill: "currentColor", className: "bi bi-search", viewBox: "0 0 16 16" },
                  React.createElement("path", { d: "M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" })
                )
              )
            )
          )
        )
      );
    }
  }]);

  return Search;
}(React.Component);

;

var MyList = function (_React$Component6) {
  _inherits(MyList, _React$Component6);

  function MyList() {
    _classCallCheck(this, MyList);

    return _possibleConstructorReturn(this, (MyList.__proto__ || Object.getPrototypeOf(MyList)).apply(this, arguments));
  }

  _createClass(MyList, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "div",
          { "class": "container text-center", style: { marginTop: "3rem" } },
          React.createElement(
            "h3",
            null,
            React.createElement(
              "b",
              null,
              "Create a List "
            )
          ),
          React.createElement(Search, null),
          " ",
          React.createElement(Filter, null),
          React.createElement(
            "div",
            null,
            React.createElement(
              "ul",
              { "class": "list-group list-group-horizontal" },
              React.createElement("li", { "class": "list-group-item flex-fill", style: { width: "55px", height: "50px" } }),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "50px" } },
                React.createElement(
                  "b",
                  null,
                  "Store"
                )
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "50px" } },
                React.createElement(
                  "b",
                  null,
                  "Item Name"
                )
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "50px" } },
                React.createElement(
                  "b",
                  null,
                  "Price"
                )
              )
            ),
            React.createElement(
              "ul",
              { "class": "list-group list-group-horizontal" },
              React.createElement(
                "li",
                { className: "list-group-item" },
                React.createElement("input", { className: "form-check-input me-1", type: "checkbox", defaultValue: "", id: "fourthCheckboxStretched" }),
                React.createElement("label", { className: "form-check-label stretched-link", htmlFor: "fourthCheckboxStretched" })
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "91px", height: "80px" } },
                "Aldi"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "Goldhen Grade A Large Eggs"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "2.55"
              )
            ),
            React.createElement(
              "ul",
              { "class": "list-group list-group-horizontal" },
              React.createElement(
                "li",
                { className: "list-group-item" },
                React.createElement("input", { className: "form-check-input me-1", type: "checkbox", defaultValue: "", id: "fifthCheckboxStretched" }),
                React.createElement("label", { className: "form-check-label stretched-link", htmlFor: "fifthCheckboxStretched" })
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "Hy-Vee"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "Farmers Hen House"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "5.07"
              )
            ),
            React.createElement(
              "ul",
              { "class": "list-group list-group-horizontal" },
              React.createElement(
                "li",
                { className: "list-group-item" },
                React.createElement("input", { className: "form-check-input me-1", type: "checkbox", defaultValue: "", id: "sixthCheckboxStretched" }),
                React.createElement("label", { className: "form-check-label stretched-link", htmlFor: "sixthCheckboxStretched" })
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "New Pioneer Co-op"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px", overflow: "hidden" } },
                "Farmers Hen House Eggs, White, 12"
              ),
              React.createElement(
                "li",
                { "class": "list-group-item flex-fill", style: { width: "90px", height: "80px" } },
                "3.49"
              )
            ),
            React.createElement("br", null),
            React.createElement(NextPage, null)
          )
        )
      );
    }
  }]);

  return MyList;
}(React.Component);

;

var Frame = function (_React$Component7) {
  _inherits(Frame, _React$Component7);

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
            padding: "0.5rem",
            width: "24rem",
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
          { className: "card-body" },
          React.createElement(MyList, null)
        ),
        React.createElement("br", null),
        React.createElement("div", { style: {
            position: "absolute",
            bottom: "0.5rem",
            right: "0.5rem"
          } }),
        React.createElement("hr", null)
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