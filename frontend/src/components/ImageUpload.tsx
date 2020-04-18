import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'


interface ImageUploadProps {
}
interface ImageUploadState {
}

export class ImageUpload extends React.Component<ImageUploadProps, ImageUploadState> {
    render() {
        return (<div className="image-upload">
            <div className="left-content">
                <header>
                    <ul>
                        <li className="left"><a href="#"><h1 className="logo">Imaginator</h1></a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">GitHub</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </header>
                <main>
                    <h1>Colorize Photos</h1>
                    <p>
                        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                    </p>
                    <div className="upload-input">
                        <input placeholder="Upload your Image..."/>
                        <button><FontAwesomeIcon icon={['fas', 'magic']} /></button>
                    </div>

                </main>
            </div>
            <div className="right-image">

            </div>
        </div>);
    }
}