import './Card.css'

export const Card = (props) => {

    return (
        <div className="cards">
            <h3 className="header3">{props.header3}</h3>
            <h1 className="header1">{props.header1}</h1>
            <p className="paragraph">{props.paragraph}</p>
            <button className="button">{props.button}</button>
        </div>
    );
}
