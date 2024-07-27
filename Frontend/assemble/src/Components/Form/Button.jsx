import { useFormStatus } from "react-dom";
import PropTypes from 'prop-types';

//This component can only be used in forms to see the status information of the form
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