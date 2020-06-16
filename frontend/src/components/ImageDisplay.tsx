import React from "react";
import ImageCompare from "image-compare-viewer";
import './styles/ImageDisplay.css';


interface ImageDisplayProps {
    original: string;
    colorized: string;
}
interface ImageDisplayState {
}

export class ImageDisplay extends React.Component<ImageDisplayProps, ImageDisplayState> {

    private viewer: any;

    componentDidMount() {
        console.log("ready!");
        //this.initComparisons();
        const options = {

            // UI Theme Defaults
            controlColor: "#FFFFFF",
            controlShadow: true,
            addCircle: false,
            addCircleBlur: true,

            // Label Defaults
            showLabels: false,
            labelOptions: {
              before: 'Before',
              after: 'After',
              onHover: false
            },
            // Smoothing
            smoothing: false,
            smoothingAmount: 100,

            // Other options
            hoverStart: false,
            verticalMode: false,
            startingPoint: 50,
            fluidMode: true
          };

        const element = document.getElementById("image-compare");
        this.viewer = new ImageCompare(element, options).mount();
    }

    componentDidUpdate(prevProps: ImageDisplayProps) {
        (document.querySelectorAll(".icv__wrapper")[0] as HTMLDivElement).style.backgroundImage = "url('" + this.props.original + "')";
        (document.querySelectorAll(".icv__fluidwrapper")[0] as HTMLDivElement).style.backgroundImage = "url('" + this.props.colorized + "')";
    }

    render() {
        return (<div id="image-compare">
                    <img src={this.props.original} alt="" />
                    <img src={this.props.colorized} alt="" />
                </div>);
    }
}