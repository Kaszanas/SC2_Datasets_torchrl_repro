from sc2_datasets.replay_parser.game_events.events.camera_update import CameraUpdate
from sc2_datasets.lightning.sc2_egset_datamodule import SC2EGSetDataModule
from multiprocessing import freeze_support
from sc2_datasets.torch.sc2_egset_dataset import SC2EGSetDataset


from tqdm import tqdm

if __name__ == "__main__":
    # For Windows support of parallel tqdm
    freeze_support()

    pytorch_dataset = SC2EGSetDataset()

    # load a couple of replays:
    len_dataset = len(pytorch_dataset)
    for i in tqdm(range(len_dataset), desc="Iterating over the dataset"):
        replay_data = pytorch_dataset[i]

        # for game_event in replay_data.gameEvents:
        #     if type(game_event).__name__ == CameraUpdate.__name__:
        #         if game_event.target is None:
        #             print("CameraUpdate event with no target!")
        #         else:
        #             print(f"CameraUpdate event with target: {game_event.target}")

    print("The entire dataset is iterable!")

    # lightning_datamodule = SC2EGSetDataModule()
