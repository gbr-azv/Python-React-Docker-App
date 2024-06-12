import './Categories.css'

export const Categories = (props) => {

    return (
        <div className="card">
            <div className={props.id}></div>
            <div className="gradient"></div>
            <p className="title">{props.id}</p>
        </div>
    );
}
