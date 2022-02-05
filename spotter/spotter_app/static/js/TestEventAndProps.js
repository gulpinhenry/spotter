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

const element = document.getElementById('clock');
ReactDOM.render(
    <Clock message={element.getAttribute("message")} />,
    element
);