import React, { RefObject } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { FileUpload } from "./FileUpload";


interface PageLayoutProps {
}
interface PageLayoutState {
}

export class PageLayout extends React.Component<PageLayoutProps, PageLayoutState> {
    private readonly imageRef: RefObject<HTMLDivElement> = React.createRef();

    constructor(props: PageLayoutProps) {
        super(props);
    }

    private manageImageResult(data: FileUpload | null) {
        if(data === null) return;
        data.uploadEvent.on((e) => {
            if(!this.imageRef.current || !e || !e.colored) return;
            this.imageRef.current.style.background = 'url(' + e.colored + ')';
        });
    }

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
                    <FileUpload ref={data => (this.manageImageResult(data))}></FileUpload>
                </main>
            </div>
            <div className="right-image" ref={this.imageRef}>
            </div>
        </div>);
    }
}