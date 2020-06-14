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
            smoothing: true,
            smoothingAmount: 100,

            // Other options
            hoverStart: false,
            verticalMode: false,
            startingPoint: 50,
            fluidMode: true
          };

        const element = document.getElementById("image-compare");
        const viewer = new ImageCompare(element, options).mount();
    }

    render() {
        return (<div id="image-compare">
                    <img src={this.props.original} alt="" />
                    <img src={this.props.colorized} alt="" />
                </div>);
    }
}