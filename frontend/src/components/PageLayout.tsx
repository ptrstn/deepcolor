import React from "react";
import { FileUpload } from "./FileUpload";
import { HeaderLinks } from "./HeaderLinks";
import { ImageDisplay } from "./ImageDisplay";


interface PageLayoutProps {
}
interface PageLayoutState {
    original: string;
    colorized: string;
}

export class PageLayout extends React.Component<PageLayoutProps, PageLayoutState> {

    constructor(props: PageLayoutProps) {
        super(props);
        this.state = {original: "/plant.JPG", colorized: "/plant_bw.JPG"};
    }

    private manageImageResult(data: FileUpload | null) {
        if(data === null) return;
        data.uploadEvent.on((e) => {
            if(!e || !e.colored || !e.original) return;
            this.setState({colorized: e.colored, original: e.original});
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
            <ImageDisplay original={this.state.original} colorized={this.state.colorized}></ImageDisplay>
        </div>);
    }
}