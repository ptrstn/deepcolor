import React from "react";


interface ImageDisplayProps {
    original: string;
    colorized: string;
}
interface ImageDisplayState {
}

export class ImageDisplay extends React.Component<ImageDisplayProps, ImageDisplayState> {

    private initComparisons() {
        Array.from(document.getElementsByClassName("img-comp-container") as HTMLCollectionOf<HTMLDivElement>)
        .forEach((e) => {
            Array.from(e.getElementsByTagName("img")).forEach(images => {
                images.width = e.getBoundingClientRect().width;
                images.height = e.getBoundingClientRect().height;
                console.log(e);
            });
        });

        Array.from(document.getElementsByClassName("img-comp-overlay") as HTMLCollectionOf<HTMLDivElement>)
        .forEach((e) => {
            this.compareImages(e);
        })
    }

    private compareImages(img: HTMLDivElement) {
        let w = img.offsetWidth;
        let h = img.offsetHeight;
        let clicked = 0;

        img.style.width = (w / 2) + "px";

        let slider = document.createElement("DIV");
        slider.classList.add("img-comp-slider");
        img.parentElement?.insertBefore(slider, img);
        slider.style.top = (h / 2) - (slider.offsetHeight / 2) + "px";
        slider.style.left = (w / 2) - (slider.offsetWidth / 2) + "px";

        slider.addEventListener("touchstart", slideReady);
        window.addEventListener("mouseup", slideFinish);

        slider.addEventListener("mousedown", slideReady);
        window.addEventListener("touchstop", slideFinish);

        function slideReady(e: { preventDefault: () => void; }) {
            e.preventDefault();
            clicked = 1;
            window.addEventListener("mousemove", slideMove);
            window.addEventListener("touchmove", slideMove);
        }
        function slideFinish() {
            clicked = 0;
        }
        function slideMove(e: MouseEvent | TouchEvent) {
            let pos;
            if (clicked === 0) return false;
            pos = getCursorPos(e)
            if (pos < 0) pos = 0;
            if (pos > w) pos = w;
            slide(pos);
        }
        function getCursorPos(e: MouseEvent | TouchEvent) {
            let a, x = 0;
            a = img.getBoundingClientRect();
            x = ((e as MouseEvent).pageX || (e as TouchEvent).touches[0].pageX) - a.left;
            x = x - window.pageXOffset;
            return x;
        }
        function slide(x: React.ReactText) {
            img.style.width = x + "px";
            slider.style.left = img.offsetWidth - (slider.offsetWidth / 2) + "px";
        }
    }

    componentDidMount() {
        console.log("ready!");
        this.initComparisons();
    }

    render() {
        return (<div className="right-image">
            <div className="img-comp-container">
                <div className="img-comp-img">
                    <img src={this.props.original} alt="Original" width="300" height="200"/>
                </div>
                <div className="img-comp-img img-comp-overlay">
                    <img src={this.props.colorized} alt="Colorized" width="300" height="200"/>
                </div>
            </div>
        </div>);
    }
}