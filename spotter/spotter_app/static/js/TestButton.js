class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return (
        <button class="btn btn-primary" onClick={() => this.setState({ liked: false })}>
          Unlike
        </button>
      )
    }

    return (
      <button class="btn btn-primary" onClick={() => this.setState({ liked: true})}>
        Like
      </button>
    )
  }
}

const element = document.querySelector('#like_button_container');
ReactDOM.render(
  <LikeButton />,
  element
);