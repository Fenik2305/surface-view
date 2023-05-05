from pyvistaqt import BackgroundPlotter
from package.figures.figure import FigureTypes
from PyQt5 import QtWidgets

class PlotterWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, window_size=[1280, 720]):
        super().__init__(parent=parent)

        self.plotter = BackgroundPlotter(show=False)
        self.plotter.enable_anti_aliasing()
        self.plotter.window_size = window_size
        
        self.plotter.enable_depth_peeling()

        self.plotter.add_axes()
        self.plotter.show_grid()
        self.plotter.enable_terrain_style(mouse_wheel_zooms=True)
        self.plotter.view_isometric()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.plotter.interactor)

        self.meshes = dict()
        self.actors = dict()
        self.actors_types = dict()
        self.actors_settings = dict()
        self.actors_HL = dict()
        self.actors_labels = dict()
        self.actors_drawed_labels = dict()
        self.intersections_list = list()

    def add_mesh(self, uid: str, mesh, figure_type, labels, **kwargs):
        if uid in self.actors:
            raise Exception("Figure already exists")
        self.meshes[uid] = mesh
        self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], **kwargs)
        self.actors_types[uid] = figure_type
        self.actors_settings[uid] = kwargs
        self.actors_labels[uid] = labels
        self.update_camera()

    def hide_mesh(self, uid: str):
        if uid not in self.actors:
            raise Exception("Figure not exist")
        self.remove_mesh(uid)
        self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], opacity=0, **self.actors_settings[uid])

    def show_mesh(self, uid: str):
        if uid not in self.actors:
            raise Exception("Figure not exist")
        self.remove_mesh(uid)
        self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], **self.actors_settings[uid])

    def remove_mesh(self, uid: str):
        if uid not in self.actors:
            raise Exception("Figure not exist")
        if uid in self.actors_HL:
            self.remove_highlight(uid)
        self.plotter.remove_actor(self.actors[uid])
        self.actors.pop(uid)
        self.update_camera()

    def highlight_mesh(self, uid: str, color: str='red', line_width: float=2.5):
        if uid not in self.actors:
                raise Exception("Figure not exist")
        if self.actors_types[uid] in [FigureTypes.CONE, FigureTypes.CYLINDER, FigureTypes.PLANE]:
            boundary = self.meshes[uid].extract_feature_edges(boundary_edges=True, non_manifold_edges=True, manifold_edges=True)
            self.actors_HL[uid] = self.plotter.add_mesh(boundary, color=color, line_width=line_width)
        elif self.actors_types[uid] in [FigureTypes.REVOLUTION]:
            self.remove_mesh(uid)
            self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], silhouette=dict(color=color, line_width=line_width), **self.actors_settings[uid])
            self.actors_HL[uid] = self.plotter.actors[list(self.plotter.actors.keys())[-2]]
        else:
            raise Exception("Unknown figure type")
        
    def remove_highlight(self, uid: str):
        self.plotter.remove_actor(self.actors_HL[uid])

    def show_edges_mesh(self, uid: str, color: str='white'):
        if uid not in self.actors:
            raise Exception("Figure not exist")
        self.remove_mesh(uid)
        self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], show_edges=True, edge_color=color, **self.actors_settings[uid])

    def hide_edges_mesh(self, uid: str):
        if uid not in self.actors_HL:
            raise Exception("Figure not exist")
        self.remove_mesh(uid)
        self.actors[uid] = self.plotter.add_mesh(self.meshes[uid], show_edges=False, **self.actors_settings[uid])

    def add_intersections(self, intersections, color='red', opacity=0.5):
        for item in intersections:
            new_intersection = self.plotter.add_mesh(item, color=color, opacity=opacity, render_lines_as_tubes=True)
            self.intersections_list.append(new_intersection)

    def remove_intersections(self):
        for item in self.intersections_list:
            self.plotter.remove_actor(item)
        self.intersections_list.clear()
        self.update_camera()

    def add_label(self, uid, point_size=14, line_width=5, font_size=12):
        meshes = self.actors_labels[uid][0]
        colors = ["green", "blue", "yellow", "purple", "cyan", "red"]
        drawed_meshes = list()
        for i in range(len(meshes)):
            drawed_meshes.append(self.plotter.add_mesh(meshes[i], color=colors[i], line_width=line_width, render_lines_as_tubes=True))
        
        points = list(self.actors_labels[uid][1].values())
        labels = list(self.actors_labels[uid][1].keys())
        self.plotter.add_point_labels(points, labels, always_visible=True, italic=True, font_size=font_size, point_color='red', point_size=point_size, show_points=True, render_points_as_spheres=True)

        drawed_points = [self.plotter.actors[list(self.plotter.actors.keys())[-2]], self.plotter.actors[list(self.plotter.actors.keys())[-1]]]
        self.actors_drawed_labels[uid] = drawed_meshes + drawed_points

    def remove_label(self, uid):
        for actor in self.actors_drawed_labels[uid]:
            self.plotter.remove_actor(actor)

    def clear_actors(self):
        for actor in list(self.actors.keys()):
            self.remove_mesh(actor)
        self.actors = dict()
        self.update_camera()

    def unlock_camera(self):
        self.fly = self.plotter.enable_fly_to_right_click()

    def lock_camera(self):
        self.update_camera()

    def update_camera(self):
        self.plotter.view_isometric()

    def get_bounds(self):
        return self.plotter.bounds
        
    def view_xy(self):
        self.plotter.view_xy()
    
    def view_xz(self):
        self.plotter.view_xz()

    def view_yx(self):
        self.plotter.view_yx()

    def view_yz(self):
        self.plotter.view_yz()
    
    def view_zx(self):
        self.plotter.view_zx()

    def view_zy(self):
        self.plotter.view_zy()

    def blur(self):
        self.plotter.add_blurring()
    
    def remove_blur(self):
        self.plotter.remove_blurring()

    def take_screenshot(self, file_name='untitled.png'):
        if file_name.split('.')[-1] not in ['png', 'jpeg', 'jpg', 'bmp', 'tif', 'tiff']:
            raise Exception("Unfortunately, this graphic format is not supported")
        self.plotter.screenshot(f"photos\{file_name}")
        