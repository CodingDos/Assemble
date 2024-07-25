import { useFormStatus } from "react-dom";
import PropTypes from 'prop-types';


function Button({pendingMessage, message}) {
    const { pending } = useFormStatus();

    return (
        <div>
            <button type="submit" disabled={pending}>
                {pending ? pendingMessage : message}
            </button>
        </div>
    )
}

Button.propTypes = {
    pendingMessage: PropTypes.string.isRequired,
    message: PropTypes.string.isRequired
}

export default Button