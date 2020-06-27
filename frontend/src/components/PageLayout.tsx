import React from "react";
import { FileUpload } from "./FileUpload";
import { HeaderLinks } from "./HeaderLinks";
import { ImageDisplay } from "./ImageDisplay";
import { Examples } from "./Examples";


interface PageLayoutProps {
}
interface PageLayoutState {
    original: string;
    colorized: string;
}

export class PageLayout extends React.Component<PageLayoutProps, PageLayoutState> {

    constructor(props: PageLayoutProps) {
        super(props);
        this.state = {original: "/examples/colorized.jpg", colorized: "/examples/grey.jpg"};
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
                <section id="header">
                    <div className="inner">
                        <h1>Welcome to <strong>Imaginator</strong>, an AI<br />
                        which can colorize your Images.</h1>
                        <p>Imaginator is an Open Source ConvNet, which lets old Images come to live.</p>
                    </div>
			    </section>
                <section id="one" className="main style1">
                    <div className="container">
                        <div className="row gtr-150">
                            <div className="col-6 col-12-medium">
                                <header className="major">
                                    <h2>Choose Your File</h2>
                                </header>
                                <p>Select the file you want to be colorized. This file will be uploaded to our server and we will process it.</p>
                            </div>
                            <FileUpload ref={data => (this.manageImageResult(data))}></FileUpload>
                            <ImageDisplay original={this.state.original} colorized={this.state.colorized}></ImageDisplay>
                        </div>
                    </div>
			    </section>
                <Examples></Examples>
            </div>
            <section id="footer">
				<ul className="icons">
					<li><a href="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col" className="icon brands alt fa-github"><span className="label">GitHub</span></a></li>
					<li><a href="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col" className="icon solid alt fa-envelope"><span className="label">Email</span></a></li>
					<li><a href="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col" className="icon solid alt fa-envelope"><span className="label">Website</span></a></li>
				</ul>
				<ul className="copyright">
					<li>&copy; Untitled</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
				</ul>
			</section>
        </div>);
    }
}