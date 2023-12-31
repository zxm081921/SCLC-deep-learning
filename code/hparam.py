class hparams:

    train_or_test = 'train'
    output_dir = 'logs/your_program_name'
    aug = False
    latest_checkpoint_file = 'checkpoint_latest.pt'
    total_epochs = 500
    epochs_per_checkpoint = 10
    batch_size = 64
    ckpt = None
    init_lr = 0.001
    scheduer_step_size = 20
    scheduer_gamma = 0.8
    debug = False
    mode = '2d' # '2d or '3d'
    in_class = 1
    out_class = 2

    crop_or_pad_size = 32,32,1 
    fold_arch = '*.png'

    source_train_0_dir = 'train/0'
    source_train_1_dir = 'train/1'
    source_test_0_dir  = 'test/0'
    source_test_1_dir  = 'test/1'
