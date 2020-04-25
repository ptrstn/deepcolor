import React, { RefObject } from "react";
import { FileUpload } from "./FileUpload";
import { HeaderLinks } from "./HeaderLinks";


interface PageLayoutProps {
}
interface PageLayoutState {
}

export class PageLayout extends React.Component<PageLayoutProps, PageLayoutState> {
    private readonly imageRef: RefObject<HTMLDivElement> = React.createRef();

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
                <HeaderLinks></HeaderLinks>
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