class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = { date: new Date() };
    }

    render() {
        return (
            <div>
                <h1>{this.props.message}</h1>
                <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
            </div>
        );
    }
}

const elements = document.getElementsByClassName('test');
for(let i = 0; i < elements.length; i++) {
    ReactDOM.render(
        <Clock message={elements[i].getAttribute("message")} />,
        elements[i]
    );
}