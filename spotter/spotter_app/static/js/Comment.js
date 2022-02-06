class Comment extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div class="react-comment">
                <h3>{this.props.author}</h3>
                <p>{this.props.content}</p>
                <p>{this.props.created}</p>
            </div>
        )
    }
}

const elements = document.getElementsByClassName("comment");
for (let i = 0; i < elements.length; i++) {
    ReactDOM.render(
        <Post author={elements[i].getAttribute("author")}
            content={elements[i].getAttribute("content")}
            created={elements[i].getAttribute("created")} />,
        elements[i]
    );
}