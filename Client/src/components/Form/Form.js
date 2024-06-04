import './Form.css';

export const Form = ({ children }) => {

    return (
        <form className='form'>
            <div className='outter-div'>
                { children }    
            </div> 
        </form>
    );
}
