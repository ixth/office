ymaps.ready(function () {
    var MAX_ZOOM = map_data.max_zoom,
        PIC_WIDTH = map_data.width,
        PIC_HEIGHT = map_data.height;

    var worldSize = Math.pow(2, MAX_ZOOM) * 256;
    var map = new ymaps.Map('map', {
            center: [0, 0],
            zoom: 0,
            controls: ['zoomControl'],
            type: new ymaps.MapType('user#customMap', [userLayer])
        }, {
            projection: new ymaps.projection.Cartesian([
                [PIC_HEIGHT - worldSize, 0],
                [PIC_HEIGHT, worldSize]
            ], [false, false]),
            restrictMapArea: [[0, 0], [PIC_HEIGHT, PIC_WIDTH]]
        });

    function userLayer() {
        var layer = new ymaps.Layer('./tiles/%z/tile-%x-%y.png');
        layer.getZoomRange = function () {
            return ymaps.vow.resolve([0, MAX_ZOOM]);
        };
        return layer;
    }
});

